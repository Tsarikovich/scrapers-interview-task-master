from fastapi import FastAPI
from .routers import queue, product

app = FastAPI()

app.include_router(queue.router, prefix="/queue", tags=["Queue"])
app.include_router(product.router, prefix="/product", tags=["Product"])
