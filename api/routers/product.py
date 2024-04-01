import aioredis
from consts import REDIS_SCRAPPED_ITEMS
from fastapi import APIRouter, Depends, HTTPException, status
import json
from typing import List

from ..models import ProductData
from ..dependencies import get_redis_pool

router = APIRouter()


@router.get("/{product_id}", response_model=ProductData, responses={
    200: {"description": "Product found"},
    404: {"description": "Product not found"}
})
async def get_product(product_id: str, redis_pool: aioredis.Redis = Depends(get_redis_pool)):
    item_key = f"{REDIS_SCRAPPED_ITEMS}:{product_id}"
    item_json = await redis_pool.get(item_key)

    if item_json is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    return ProductData(data=json.loads(item_json))


@router.get("/", response_model=List[ProductData], responses={
    200: {"description": "List of products"},
    204: {"description": "No products found"}
})
async def list_products(redis_pool: aioredis.Redis = Depends(get_redis_pool)):
    keys = await redis_pool.smembers(REDIS_SCRAPPED_ITEMS)
    products: List[ProductData] = []

    for key in keys:
        item_json = await redis_pool.get(key)
        if item_json:
            item = json.loads(item_json)
            products.append(ProductData(data=item))

    return products
