from fastapi import FastAPI
from database import db
import users
import items
import orders
import uvicorn

app = FastAPI(title='Task 6')


app.include_router(users.router, tags=['Users'])
app.include_router(items.router, tags=['Items'])
app.include_router(orders.router, tags=['Orders'])


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
