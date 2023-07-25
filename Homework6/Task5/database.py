import motor.motor_asyncio
from settings import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
db = client.my_base
tasks_collection = db.get_collection("task_collection")


