import logging
from mongoengine import connect, disconnect
from decouple import config

from api.repositories.client_repository import ClientRepository

# logger = logging.getLogger("uvicorn.error")


def get_client_repo():
    # logger('Connecting to the database')
    connect('clients', host=config('MONGO_URL'))
    return ClientRepository()
