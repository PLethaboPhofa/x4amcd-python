from redis import Redis

redisApi = Redis(host='localhost', port=6379, decode_responses=True)

def get(key):
    return redisApi.get(key)

def set(key, value):
    return redisApi.set(key, value)