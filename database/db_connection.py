from motor.motor_asyncio import AsyncIOMotorClient
from settings import settings
async def connect_insert(id, height, weight):

    cluster = AsyncIOMotorClient(settings.MONGO_URI)
    try:
        db = cluster[settings.MONGO_DB_NAME]
        collection = db.Users_Data
        data = {"cliet_id": id, "height": height, "weight": weight}
        await collection.insert_one(data)
    finally:
        cluster.close()
