import redis
import threading

# Connection to Valkey
redis_client = redis.from_url(
  'rediss://solhealth-9gydt8.serverless.use1.cache.amazonaws.com:6379',
  health_check_interval=10,
  socket_connect_timeout=5,
  retry_on_timeout=True,
  socket_keepalive=True
)
1
user_id = 1
session_id = "9fd6b88f-03a8-42ea-ac4d-59767dc1648e"
redis_key = f"session:{user_id}:{str(session_id)}"
prev_messages = redis_client.lrange(redis_key, 0, -1)
print("All Good")
print(prev_messages)

