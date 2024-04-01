import os
import json
from scrapy.http.response import Response, Request
from scrapy_redis.spiders import RedisSpider
from ..items import ProductItem
from consts import REDIS_QUEUE
from typing import Generator


class TiktokShopSpider(RedisSpider):
    """
       A spider for scraping product information from TikTok shop.
       This spider listens on a Redis queue for product IDs and fetches product data from the TikTok API.
    """
    name = "tiktok_shop_spider"
    redis_key = REDIS_QUEUE
    allowed_domains = ['tiktokv.com']
    endpoint = 'https://oec16-normal-useast5.us.tiktokv.com/api/v1/shop/product_info/get?&carrier_region=US&locale=en'

    def __init__(self, *args, **kwargs):
        super(TiktokShopSpider, self).__init__(*args, **kwargs)
        self.headers = {
            "Accept-Encoding": "gzip",
            "Connection": "Keep-Alive",
            "Content-Type": "application/json; charset=UTF-8",
            "User-Agent": os.getenv('USER_AGENT'),
        }

    def make_request_from_data(self, data: bytes) -> Request:
        product_id = data.decode('utf-8')

        cookies = {
            "store-idc": "useast5",
            "sid_tt": os.getenv('SID_TT'),
            "store-country-code": "us",
        }

        body_data = {"product_id": [product_id]}
        return Request(
            url=self.endpoint,
            method='POST',
            headers=self.headers,
            cookies=cookies,
            body=json.dumps(body_data),
            callback=self.parse
        )

    def parse(self, response: Response) -> Generator[Request, None, None]:
        data_json = json.loads(response.text)
        data = data_json.get('data', {})

        if not data:
            return

        products = data.get('products', [])
        for product_data in products:
            item = ProductItem()
            item.fill_from_product_data(product_data)
            item['proxy'] = response.meta.get('proxy')
            yield item
