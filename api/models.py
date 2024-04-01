from typing import List, Dict, Any
from pydantic import BaseModel, Field


class ProductIDs(BaseModel):
    product_ids: List[str] = Field(
        ...,
        description="A list of product IDs to be processed or retrieved.",
        example=["12345", "67890", "abcde"]
    )


class ProductData(BaseModel):
    data: Dict[str, Any] = Field(
        ...,
        description="A dictionary containing all the relevant data for a product.",
        example={
            "product_id": "12345",
            "name": "Cool Product",
            "description": "A very cool product you must have!",
            "price": 19.99,
            "in_stock": True
        }
    )
