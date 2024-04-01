import random
from scrapy import Spider
from scrapy.exceptions import IgnoreRequest
from scrapy.http import Request, Response
from typing import List, Optional


class Proxy:
    def __init__(self, ip: str, port: str, username: Optional[str] = None, password: Optional[str] = None):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def __str__(self):
        if self.username and self.password:
            return f"http://{self.username}:{self.password}@{self.ip}:{self.port}"
        return f"http://{self.ip}:{self.port}"


class ProxyMiddleware:
    def __init__(self, proxy_list_path: str):
        self.proxies: List[Proxy] = []
        self.load_proxies(proxy_list_path)

    def load_proxies(self, path: str):
        if not path:
            return

        try:
            with open(path, 'r') as file:
                for line in file:
                    parts = line.strip().split(':')
                    if len(parts) == 4:
                        self.proxies.append(Proxy(*parts))
                    elif len(parts) == 2:
                        self.proxies.append(Proxy(parts[0], parts[1]))
        except FileNotFoundError:
            raise Exception(f"Proxy file not found: {path}")

    def process_request(self, request: Request, spider: Spider):
        if 'proxy' not in request.meta:
            proxy = random.choice(self.proxies)
            request.meta['proxy'] = str(proxy)
            spider.logger.info(f"Proxy assigned: {request.meta['proxy']}")

    def process_response(self, request: Request, response: Response, spider: Spider):
        if response.status in [403, 429, 502, 503] or not response.text:
            retry_count = request.meta.get('retry_count', 0)
            retry_limit = spider.crawler.settings.getint('RETRY_LIMIT', 3)

            if retry_count < retry_limit:
                spider.logger.info(
                    f"Bad proxy, retrying with a new one. Retry count: {retry_count}")
                retry_count += 1
                request.meta['retry_count'] = retry_count
                request.dont_filter = True
                del request.meta['proxy']
                return self.process_request(request, spider) or request
            else:
                spider.logger.error(f"Retry limit reached for URL: {request.url}. Abandoning request.")
                raise IgnoreRequest()
        return response

    def process_exception(self, request: Request, exception: Exception, spider: Spider):
        retry_count = request.meta.get('retry_count', 0)
        retry_limit = spider.crawler.settings.getint('RETRY_LIMIT', 3)

        if retry_count < retry_limit:
            spider.logger.info(f"Exception {exception} with proxy: {request.meta.get('proxy')}, retrying...")
            retry_count += 1
            request.meta['retry_count'] = retry_count
            request.dont_filter = True
            del request.meta['proxy']
            self.process_request(request, spider)
            return request
        else:
            spider.logger.error(
                f"Retry limit reached for URL: {request.url} after exception {exception}. Abandoning request.")
            raise IgnoreRequest()

    @classmethod
    def from_crawler(cls, crawler):
        proxy_list_path = crawler.settings.get('PROXY_LIST_PATH')
        return cls(proxy_list_path)

    def spider_opened(self, spider):
        spider.logger.info(f"Loaded {len(self.proxies)} proxies.")
