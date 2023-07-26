from fastapi import FastAPI
from database import db
import tasks
import uvicorn

app = FastAPI(title='Task 5')


app.include_router(tasks.router, tags=['Tasks'])


# @app.on_event("startup")
# async def startup():
#     await db.connect()
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     await db.disconnect()

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
