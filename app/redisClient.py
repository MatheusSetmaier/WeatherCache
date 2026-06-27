import os
import redis

redis_url = os.getenv('REDIS_HOST')

if redis_url and redis_url.startswith('redis://'):
    redis_client = redis.from_url(
        redis_url,
        decode_responses = True
    )
else:
    redis_client = redis.Redis(
        host = os.getenv('REDIS_HOST', 'localhost'),
        port = int(os.getenv('REDIS_PORT', 6379)),
        decode_responses = True
    )