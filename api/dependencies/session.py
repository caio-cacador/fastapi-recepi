from api.services.logger import LOGGER
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from decouple import config


def get_mongodb_client() -> AsyncIOMotorCollection:
    LOGGER.info('Connecting to the database')
    return AsyncIOMotorClient(config("MONGO_URL"))
