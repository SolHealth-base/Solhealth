import os
import json
import redis
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("REDIS_ENDPOINT")
port = os.getenv("REDIS_PORT")
password = os.getenv("REDIS_PASSWORD")

redis_client = redis.Redis(
  host=endpoint,
  port=port,
  password=password)


def init_reddis_storage(user_id, conv_id):

    user_conv = []
    conv_dicts = {conv_id:user_conv}
    
    dicts_serialized = {key: json.dumps(value) for key, value in conv_dicts.items()}
    redis_client.hset(f"{user_id}:1", mapping= dicts_serialized)
    print("Storage Initialized")

def reddis_init_storage_with_mongo(user_id, conv_id, conv_dicts):

    conv_dicts = {conv_id:conv_dicts}
    dicts_serialized = {key: json.dumps(value) for key, value in conv_dicts.items()}
    
    redis_client.hset(f"{user_id}:1", mapping= dicts_serialized)
    print("Storage Initialized")

def get_conversation(user_id, conv_id = "conv1"):

    chat_history = redis_client.hget(f"{user_id}:1", conv_id)
    if chat_history:
        conversation = json.loads(chat_history.decode("utf-8"))
    else:
        conversation = []

    return conversation
       
def update_conversation(user_id, chat_history, user_query, bot_response):

    chat_history_update = chat_history
    chat_history_update.extend([user_query, bot_response])

    if (len(chat_history_update) >= 30):
        chat_history_update = chat_history_update[1:]

    redis_client.hset(f"{user_id}:1", "conv1", json.dumps(chat_history_update))

    return chat_history_update


def handle_conversation(user_id, new_query):

    chat_history = get_conversation(user_id)
    chat_history_update = update_conversation(chat_history, new_query)
       
    redis_client.hset(f"{user_id}:1", "conv1", json.dumps(chat_history_update))

    return chat_history

def delete_storage(user_id):

    redis_client.delete(f"{user_id}:1")
    print("Deleted")

