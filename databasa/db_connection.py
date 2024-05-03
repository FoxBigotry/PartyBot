from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_BD

async def connect_insert(id,height,weight):
    cluster = AsyncIOMotorClient(MONGO_BD)
    db = cluster.PartyBot
    collection = db.Users_Data
    data = {"cliet_id": id, "height": height, "weight": weight}
    await collection.insert_one(data)
    cluster.close()