from pydantic import BaseModel, Field
from settings import settings
from decimal import Decimal


class ItemIn(BaseModel):
    name: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    description: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    cost: Decimal = Field(..., max_digits=10, decimal_places=2)


class Item(ItemIn):
    id: int
