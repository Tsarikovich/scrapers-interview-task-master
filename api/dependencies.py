import aioredis
from .config import settings


async def get_redis_pool():
    redis = aioredis.from_url(settings.redis_url, encoding="utf8", decode_responses=True)
    try:
        yield redis
    finally:
        await redis.close()
