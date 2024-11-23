import os
import sys
from flask import Flask, jsonify, request
from backend.services.chatbot_service import handle_user_message
from flask_cors import CORS


# Initialize the Flask app
appl = Flask(__name__)
CORS(appl)


# Define the default route
@appl.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok"}), 200

# Define the route to handle the chatbot input
@appl.route('/chat', methods=['POST'])
def chat():

    data = request.get_json()
    user_id = data['user_id']
    user_query = data["query"]
    response = handle_user_message(user_id, user_query)

    return jsonify({'response': response})
