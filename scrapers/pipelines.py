import redis
import json
from scrapy import Spider, Item
from scrapy.exceptions import DropItem
from consts import REDIS_SCRAPPED_ITEMS


class RedisPipeline:
    """
    Pipeline for storing scraped items in Redis.
    Utilizes a combination of SET for individual items and a SET collection for tracking item keys.
    """

    def __init__(self, redis_host: str, redis_port: int, redis_db: int):
        self.redis_conn: redis.Redis | None = None
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.redis_db = redis_db

    @classmethod
    def from_crawler(cls, crawler):
        """Instantiate pipeline using settings from the crawler."""
        return cls(
            redis_host=crawler.settings.get('REDIS_HOST', 'redis'),
            redis_port=crawler.settings.get('REDIS_PORT', 6379),
            redis_db=crawler.settings.get('REDIS_DB', 0)
        )

    def open_spider(self, spider: Spider):
        """Initialize the Redis connection."""
        self.redis_conn = redis.Redis(host=self.redis_host, port=self.redis_port, db=self.redis_db)

    def close_spider(self, spider: Spider):
        """Close the Redis connection."""
        self.redis_conn.close()

    def process_item(self, item: Item, spider: Spider) -> Item:
        """Process and store each item in Redis."""
        try:
            item_json = json.dumps(dict(item))
            product_id = item.get('id')
            if not product_id:
                raise DropItem("Missing product ID in item.")
            item_key = f"{REDIS_SCRAPPED_ITEMS}:{product_id}"

            self.redis_conn.set(item_key, item_json)
            self.redis_conn.sadd(REDIS_SCRAPPED_ITEMS, item_key)

            spider.logger.info(f"Saved item {item_key}")
            return item

        except redis.RedisError as e:
            spider.logger.error(f"Failed to save item {product_id=} to Redis: {e}")
            raise DropItem(f"Redis error: {e}")
