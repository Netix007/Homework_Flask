from fastapi import APIRouter, HTTPException
from order_models import Order, OrderIn, OrderOut
from database import orders, db


router = APIRouter()


@router.get("/orders", response_model=list[OrderOut])
async def get_orders():
    query = "select orders.id, orders.order_date, users.first_name, users.last_name, users.email, " \
            "items.name as item_name, items.description as item_description, items.cost, orders.is_done from orders " \
            "join items on items.id = orders.item_id " \
            "join users on users.id = orders.user_id"
    return await db.fetch_all(query=query)


@router.post("/orders", response_model=Order)
async def create_order(item: OrderIn):
    query = orders.insert().values(**item.model_dump())
    order_id = await db.execute(query=query)
    return Order(**item.model_dump(), id=order_id)


@router.get("/orders/{order_id}", response_model=Order)
async def get_order_by_id(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    data = await db.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=404, detail="Order not found")
    return data


@router.put("/orders/{order_id}", response_model=Order)
async def update_order(order_id: int, order: OrderIn):
    query = orders.update().where(orders.c.id == order_id).values(**order.model_dump())
    res = await db.execute(query=query)
    if res > 0:
        return Order(**order.model_dump(), id=order_id)
    raise HTTPException(status_code=404, detail="Order not found")


@router.delete("/orders/{order_id}", response_model=dict)
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    res = await db.execute(query=query)
    if res > 0:
        return {"message": "Order was successfully deleted"}
    raise HTTPException(status_code=404, detail="Order not found")
