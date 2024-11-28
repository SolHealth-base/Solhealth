import requests

wallet_add = "wefsevzsdovnozsnvz"
username = "fresh"

# url = f"http://127.0.0.1:9697/add_user/{username}/{wallet_add}"
# response = requests.post(url).json()
# print(response)

user_id = 1
session_id = "9fd6b88f-03a8-42ea-ac4d-59767dc1648e"
url = f"http://127.0.0.1:9697/get_response/{user_id}/{session_id}"

input_dicts = {"query": "Hi"}
response = requests.post(url, json=input_dicts).json()
print(response['message'])


# url = f"http://127.0.0.1:9697/start_new_session/1"
# response = requests.post(url).json()
# print(response)


# url = f"http://127.0.0.1:9697/end_session/1/9fd6b88f-03a8-42ea-ac4d-59767dc1648e"
# response = requests.post(url).json()
# print(response)

# url = f"http://127.0.0.1:9697/pull_session/1/9fd6b88f-03a8-42ea-ac4d-59767dc1648e"
# response = requests.post(url).json()
# print(response)

# url = f"http://127.0.0.1:9697/get_response/1/3b4e9def-9f44-4c26-b0c3-cf278d1eb046"
# for i in range(3):

#     inputs = input("Enter your query: \n")
#     dicts = {"query": inputs}
#     response = requests.post(url, json=dicts).json()
#     print(response['message'])