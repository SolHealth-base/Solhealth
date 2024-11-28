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


def pull_conversation(user_id, conv_id = "conv1"):

    chat_history = redis_client.hget("chathistory:1", user_id)
    conversation = json.loads(chat_history.decode("utf-8"))
    return conversation

def get_conversation(user_id, conv_id = "conv1"):

    chat_history = pull_conversation(user_id)
    chat_history = chat_history[conv_id]

    return chat_history
       
def update_conversation(chat_history, new_query, conv_id = 'conv1'):

    chat_history_update = chat_history
    chat_history_update.append(new_query)

    if (len(chat_history_update) >= 10):
        chat_history_update = chat_history_update[1:]

    chat_history_update = {conv_id: chat_history_update}
    redis_client.hset('chathistory:1', "user1", json.dumps(chat_history_update))

    return chat_history_update

def handle_conversation(user_id, new_query, conv_id = 'conv1'):

    chat_history = get_conversation(user_id, conv_id)
    chat_history_update = update_conversation(chat_history, new_query)
       
    redis_client.hset('chathistory:1', "user1", json.dumps(chat_history_update))

    return chat_history

for i in range(10):

    query = input("Wha's up?\n")
    history = get_conversation("user1")
    print(history)
    update_conversation(history, query)