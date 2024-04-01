import aioredis
from consts import REDIS_QUEUE
from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies import get_redis_pool
from ..models import ProductIDs

router = APIRouter()


@router.post("/", status_code=status.HTTP_202_ACCEPTED, responses={
    202: {"description": "Items enqueued successfully"},
    400: {"description": "Bad request, no product IDs provided"}
})
async def enqueue_items(items: ProductIDs, redis_pool: aioredis.Redis = Depends(get_redis_pool)):
    if not items.product_ids:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No product IDs provided")

    for product_id in items.product_ids:
        await redis_pool.lpush(REDIS_QUEUE, product_id)

    return {"message": "Items enqueued", "product_ids": items.product_ids}


@router.get("/", response_model=ProductIDs, responses={
    200: {"description": "List of product IDs in the queue"},
    204: {"description": "No product IDs found in the queue"}
})
async def list_queue_items(redis_pool: aioredis.Redis = Depends(get_redis_pool)):
    items = await redis_pool.lrange(REDIS_QUEUE, 0, -1)
    if not items:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No product IDs found in the queue")

    product_ids = [item for item in items]
    return ProductIDs(product_ids=product_ids)
