from datetime import datetime

from scrapy.item import Item, Field
from typing import Dict, Any


class ProductItem(Item):
    """
    Item to store product data scraped from TikTok shop.
    """
    id = Field(serializer=str)
    url = Field(serializer=str)
    seller = Field(serializer=dict)
    product_base = Field(serializer=dict)
    sale_props = Field(serializer=dict)
    logistic = Field(serializer=dict)
    scraping_time = Field(serializer=str)
    proxy = Field(serializer=str)

    def fill_from_product_data(self, product_data: Dict[str, Any]) -> None:
        """
        Populates the item fields with data extracted from the product information.

        :param product_data: A dictionary containing the product data.
        """
        self['id'] = product_data.get('product_id')
        self['url'] = product_data.get('share_info', {}).get('share_deep_link')
        self['seller'] = product_data.get('seller', {})
        self['product_base'] = product_data.get('product_base', {})
        self['sale_props'] = product_data.get('sale_props', [])
        self['logistic'] = product_data.get('logistic', {})
        self['scraping_time'] = datetime.now().isoformat()
