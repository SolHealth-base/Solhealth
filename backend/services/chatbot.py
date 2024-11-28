from flask_cors import CORS
from flask import Flask, jsonify, request
from chatbot_service import handle_user_query, generate_title

from uuid import uuid4
from datetime import datetime
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://fresh:fresh24@localhost/chatbot'
#app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{dbname}'
db = SQLAlchemy(app)

# Define database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    wallet_address = db.Column(db.String(255), unique=True, nullable = False)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    session_id = db.Column(db.String(36), default=str(uuid4()), unique=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    session_title = db.Column(db.String(255), unique=True, nullable = False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(36), db.ForeignKey('session.session_id'))
    sender = db.Column(db.String(255))
    message = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=db.func.now())

# This creates all tables in the database that are defined in the models
with app.app_context():
    db.create_all()


# Define the default route
@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok"}), 200

@app.route('/add_user/<username>/<wallet_address>', methods=['POST'])
def add_user(username, wallet_address):
    
    user = User(username=username, wallet_address=wallet_address)
    db.session.add(user)
    db.session.commit()

    return {"status": "user added"}, 200

@app.route('/start_new_session/<user_id>', methods=['POST'])
def start_new_session(user_id):

    inputs = request.get_json()
    query = inputs['query']
    title = generate_title(query)

    session_id = str(uuid4())
    new_session = Session(user_id=user_id, session_id=session_id, session_title=title)
    db.session.add(new_session)
    db.session.commit()

    return {"status": "session created"}, 200

@app.route('/pull_session/<user_id>/<session_id>', methods=['POST'])
def pull_session(user_id, session_id):

    session = Session.query.filter_by(user_id=user_id, session_id=session_id).first()

    if session:

        messages = Message.query.filter_by(session_id=session_id).all()
        messages_data = [
                {msg["sender"]: msg["message"]}
                for msg in messages
            ]
            
        return {'status': 'Successfully!', "messages": messages_data}, 200
    else:
        # Return a message if no session is found
        return {'status': 'Session not found!', "messages": []}, 404

@app.route('/get_titles/<user_id>', methods=['POST'])  
def get_titles(user_id):

    sessions = Session.query.filter_by(user_id=user_id).all()
    if sessions:
        titles = [session.session_title for session in sessions]
        return {'status': 'Successful', "tiles": titles}, 404

    else:
        return {'status': 'No session not found!'}, 404

    
def update_sessions(user_id, session_id, messages):

    session = Session.query.filter_by(user_id=user_id, session_id=session_id).first()
    if session:
        
        last_message = Message.query.filter_by(session_id=session_id).order_by(Message.timestamp.desc()).first()
        if last_message:
            new_messages = []
            for message in messages:

                sender, message = message["sender"], message["message"]
                message = Message(session_id=session_id, sender=sender, message=message)
                new_messages.append(message)
        # Bulk insert all the new messages at once
        db.session.bulk_save_objects(new_messages)
        db.session.commit()


@app.route('/get_response/<user_id>/<session_id>', methods=['POST'])
def get_response(user_id, session_id):
   
    data = request.get_json()
    user_query = data["query"]
    
    session = pull_session(user_id, session_id)
    prev_messages = session['messages']

    response = handle_user_query(user_query, prev_messages)
    db_message_update = [{"sender": "user", "message":user_query},
                         {"sender": "bot", "message":response} ]
    update_sessions(db_message_update)

    return {"status": "Successful", "message": response}, 200

@app.route('/end_session/<user_id>/<session_id>', methods=['POST'])
def end_session(user_id, session_id):
 
    messages = [item.decode('utf-8') for item in messages]
    session = Session.query.filter_by(user_id=user_id, session_id=session_id).first()
    new_messages = []
    if session:

        last_message = Message.query.filter_by(session_id=session_id).order_by(Message.timestamp.desc()).first()

        if last_message:
 
            for msg in messages:
                sender, message = last_message.sender, last_message.message 

                # Only add messages that come after the last message (based on timestamp or ID)
                if last_message:
                    # Compare based on timestamp or ID; assuming timestamp here
                    if last_message.timestamp < datetime.datetime.now():  # You can compare with last_message.timestamp if needed
                        new_message = Message(session_id=session_id, sender=sender, message=message)
                        new_messages.append(new_message)
        
        else:
            # Save messages to PostgreSQL
            for msg in messages:
                new_message = Message(session_id=session_id, sender=msg.split(": ")[0], message=msg.split(": ")[1])
                new_messages.append(new_message)

        # Bulk insert all the new messages at once
        db.session.bulk_save_objects(new_messages)
        db.session.commit()

        
        return {"status": "session ended"}, 200
    else:
        return {"status": "session not found"}, 404

if __name__ == '__main__':
    app.run(debug = True, port=9697)


