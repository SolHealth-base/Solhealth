from pymongo import MongoClient
from app.config import config
from pymongo.server_api import ServerApi



username = config["development"].MONGO_DB_USERNAME
password = config["development"].MONGO_DB_PASSWORD

uri = f"mongodb+srv://{username}:{password}@solhealth.ovcfg.mongodb.net/?retryWrites=true&w=majority&appName=Solhealth"
client = MongoClient(uri, server_api=ServerApi('1'))

user_db = client["user_db"]
collection = user_db["chatbot_history"]

# Function to store a conversation
def update_conversation(user_id, new_messages, conversations):

    # Update the specific conversation within the conversations array

    new_message = new_messages['messages']
    conversation_id = new_messages['conversation_id']

    conversations = conversations['conversations'][0]['messages']
    conversations.extend(new_message)

    collection.update_one(
        {"user_id": user_id, "conversations.conversation_id": conversation_id},  # Find the user and specific conversation
        {"$set": {"conversations.$.messages": conversations}}  # Push new messages into the specific conversation
    )

# Function to get all conversation IDs for a user
def get_conversation_ids(user_id):
    # Query to get the user's document and project only conversation IDs
    user_data = collection.find_one(
        {"user_id": user_id},          # Filter by user_id
        {"_id": 0, "conversations.conversation_id": 1}  # Only return conversation_id fields
    )
    
    # If the user is found, extract the conversation_ids
    if user_data and "conversations" in user_data:
        conversation_ids = [conv["conversation_id"] for conv in user_data["conversations"]]
        return conversation_ids
    else:
        return f"No conversations found for user: {user_id}"

def move_data_from_redis_to_mongodb(user_id, conversation_id, messages):
    # Check if the conversation exists
    conversation_exists = collection.find_one(
        {"user_id": user_id, "conversations.conversation_id": conversation_id}
    )

    # Create a new conversation object
    conversation = {
        "conversation_id": conversation_id,
        "messages": messages
    }

    # If conversation exists, append messages
    if conversation_exists:
        update_conversation(user_id, conversation, conversation_exists)

    else:
        # If not, create a new conversation
        collection.update_one(
            {"user_id": user_id},
            {"$push": {"conversations": conversation}},
            upsert=True
        )

def retrieve_consersation(user_id, conversation_id = None):


    if conversation_id:

        user_data = collection.find_one(
            {"user_id": user_id, "conversations.conversation_id": conversation_id},
            {"conversations.$": 1}  # Only return the matching conversation
        )

        if user_data:
            return user_data["conversations"][0]["messages"][-20:]  # Return the specific conversation
        
        else:
            return None

    # If no conversation_id is provided, retrieve all conversations
    user_data = collection.find_one({"user_id": user_id}, {"_id": 0, "conversations": 1})
    if user_data:
        return user_data["conversations"]  # Return all conversations
    else:
        return f"No chat history found for user: {user_id}"


# def move_data_from_redis_to_mongodb():

#     ""


# scheduler.add_job(move_data_from_redis_to_mongodb, 'interval', minutes=5, args = (user_id, conv_id, messages))



# scheduler.start()

# # Keep the script running (since APScheduler runs in the background)
# try:
#     while True:
#         time.sleep(2)
# except (KeyboardInterrupt, SystemExit):
#     scheduler.shutdown()
