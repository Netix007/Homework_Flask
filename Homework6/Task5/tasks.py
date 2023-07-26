from fastapi import APIRouter, Body, HTTPException, status
from models import TaskModel, UpdateTaskModel
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from database import db
from typing import List


router = APIRouter()


@router.get("/tasks", response_model=List[TaskModel])
async def list_tasks():
    print(await db["task_collection"].find().to_list(1000))
    return await db["task_collection"].find().to_list(1000)


@router.post("/tasks", response_description="Add new task", response_model=TaskModel)
async def create_task(task: TaskModel = Body(...)):
    task = jsonable_encoder(task)
    new_task = await db["newtasks"].insert_one(task)
    created_task = await db["newtasks"].find_one({"_id": new_task.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_task)
#
#
# @router.get("/items/{item_id}", response_model=Item)
# async def get_item_by_id(item_id: int):
#     query = items.select().where(items.c.id == item_id)
#     data = await db.fetch_one(query=query)
#     if not data:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return data
#
#
# @router.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: int, item: ItemIn):
#     query = items.update().where(items.c.id == item_id).values(**item.model_dump())
#     res = await db.execute(query=query)
#     if res > 0:
#         return Item(**item.model_dump(), id=item_id)
#     raise HTTPException(status_code=404, detail="Item not found")
#
#
# @router.delete("/items/{item_id}", response_model=dict)
# async def delete_item(item_id: int):
#     query = items.delete().where(items.c.id == item_id)
#     res = await db.execute(query=query)
#     if res > 0:
#         return {"message": "Item was successfully deleted"}
#     raise HTTPException(status_code=404, detail="Item not found")