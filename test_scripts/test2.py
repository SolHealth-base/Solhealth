import os
import ast
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

       
def store_conversation(user_id, new_query, conv_id = 'conv1'):

    chat_response = redis_client.hget(f"{user_id}:1", conv_id)
    chat_response = json.loads(chat_response.decode("utf-8"))
    chat_response.append(new_query)

    if (len(chat_response) >= 10):
        chat_response = chat_response[1:]
    
    redis_client.hset('chathistory:1', "user1", json.dumps(chat_response))

def get_conversation(user_id, conv_id = "conv1"):

    chat_response = redis_client.hget(f"{user_id}:1", conv_id)
    chat_response = json.loads(chat_response.decode("utf-8"))

    return chat_response

def update_conversation(chat_history, new_query, conv_id = 'conv1'):

    chat_history_update = chat_history
    chat_history_update.append(new_query)

    if (len(chat_history_update) >= 10):
        chat_history_update = chat_history_update[1:]

    return chat_history_update

def handle_conversation(user_id, new_query):

    chat_history = get_conversation(user_id)
    chat_history_update = update_conversation(chat_history, new_query)
       
    redis_client.hset("user1:1", "conv1", json.dumps(chat_history_update))

    return chat_history


# user1_conv1 = ["How are you doing", "I'm very well. Thanks"]
# user2_conv1 = ["Hi, There", "No hying please"]

# user_1 = {"conv1": user1_conv1}
# user_2 = {"conv1": user2_conv1}

# dicts = {"conv1": user1_conv1, "conv2": user2_conv1}
# dicts_serialized = {key: json.dumps(value) for key, value in dicts.items()}
# redis_client.hset("user1:1", mapping= dicts_serialized)

# for i in range(5):
    
#     query = input("What's up?\n")
#     chat_response = redis_client.hget("user1:1", "conv1")
#     response = handle_conversation("user1", query)
#     chat_response = redis_client.hget("user1:1", "conv1")
#    # print(chat_response)



# # Your existing conversation data


# # Serialize the data to JSON before storing
# dicts_serialized = {key: json.dumps(value) for key, value in dicts.items()}

# # Store the serialized data in Redis
# redis_client.hset('chathistory:1', mapping=dicts_serialized)

redis_client.delete("user1:1")
print("Deleted")