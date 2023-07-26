from fastapi import APIRouter, HTTPException
from item_models import Item, ItemIn
from database import items, db


router = APIRouter()


@router.get("/items", response_model=list[Item])
async def get_items():
    return await db.fetch_all(items.select())


@router.post("/items", response_model=Item)
async def create_item(item: ItemIn):
    query = items.insert().values(**item.model_dump())
    item_id = await db.execute(query=query)
    return Item(**item.model_dump(), id=item_id)


@router.get("/items/{item_id}", response_model=Item)
async def get_item_by_id(item_id: int):
    query = items.select().where(items.c.id == item_id)
    data = await db.fetch_one(query=query)
    if not data:
        raise HTTPException(status_code=404, detail="Item not found")
    return data


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemIn):
    query = items.update().where(items.c.id == item_id).values(**item.model_dump())
    res = await db.execute(query=query)
    if res > 0:
        return Item(**item.model_dump(), id=item_id)
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/items/{item_id}", response_model=dict)
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    res = await db.execute(query=query)
    if res > 0:
        return {"message": "Item was successfully deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
