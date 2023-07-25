from pydantic import BaseModel, Field, EmailStr
from datetime import date
from decimal import Decimal


class OrderIn(BaseModel):
    user_id: int
    item_id: int
    order_date: date = Field(..., format="%Y-%m-%d")
    is_done: bool = False


class Order(OrderIn):
    id: int


class OrderOut(BaseModel):
    id: int
    order_date: date = Field(..., format="%Y-%m-%d")
    first_name: str
    last_name: str
    email: EmailStr
    item_name: str
    item_description: str
    cost: Decimal
    is_done: bool
