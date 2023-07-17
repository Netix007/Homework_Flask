from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from enum import Enum


app = FastAPI(title="FastAPI App")


class Status(Enum):
    TO_DO = "todo"
    IN_PROGRESS = "in progress"
    DONE = "done"


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: Status


class TaskModel(BaseModel):
    title: str
    description: Optional[str]
    status: Status


tasks = [Task(id=1, title="title", description=None, status=Status.DONE)]


@app.get("/")
async def get_tasks():
    return {"message": "FastAPI works!"}


@app.get("/tasks", response_model=list[Task])
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def get_item_by_id(task_id: int):
    task = [task for task in tasks if task.id == task_id]
    if task:
        return task[0]
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
async def create_task(task: TaskModel):
    next_id = max(tasks, key=lambda x: x.id).id + 1
    new_task = Task(id=next_id, title=task.title, description=task.description, status=task.status)
    tasks.append(new_task)


@app.put("/tasks/{task_id}")
async def change_task(task_id: int, task: TaskModel):
    update_task = [t for t in tasks if t.id == task_id]
    if not update_task:
        raise HTTPException(status_code=404, detail="Task not found")
    update_task[0].title = task.title
    update_task[0].description = task.description
    update_task[0].status = task.status
    return update_task[0]


@app.delete("/tasks/{task_id}")
async def get_item_by_id(task_id: int):
    task = [task for task in tasks if task.id == task_id]
    if task:
        tasks.remove(task[0])
        return task_id
    raise HTTPException(status_code=404, detail="Task not found")
