from api.services.logger import LOGGER
from typing import List
from pymongo import ReturnDocument
from bson.objectid import ObjectId
from api.dependencies.session import get_mongodb_client
from api.models.client import ClientModel
from api.exceptions.repo_exceptions import ClientCanNotBeUpdatedError, ClientNotFoundError, ClientStatusError


class ClientRepository:

    def __init__(self) -> None:
        db = get_mongodb_client()
        self.clients = db['client']['clients']

    async def _get_by_id(self, id) -> dict:
        id_ = id if isinstance(id, ObjectId) else ObjectId(id)
        client = await self.clients.find_one({'_id': id_})
        if not client:
            raise ClientNotFoundError(client_id=id)
        return client
    
    async def get_model_by_id(self, id: str) -> ClientModel:
        client = await self._get_by_id(id)
        return ClientModel.from_mongo(client)

    async def update(self, client: ClientModel) -> dict:
        update = {k: v for k, v in client.dict().items() if v is not None}
        result = await self.clients.find_one_and_update(
            {'_id': ObjectId(client.id)},
            {'$set': update},
            return_document=ReturnDocument.AFTER
        )
        if result:
            return ClientModel.from_mongo(result)
        raise ClientNotFoundError(client_id=id)

    async def update_client_personal_info(
        self,
        id: str, 
        name: str = None, 
        document: str = None
      ) -> ClientModel:

        client = await self.get_model_by_id(id)
        if client.active is False:
            raise ClientCanNotBeUpdatedError(client_id=id)

        if name:
            client.name = name
        if document:
            client.document = document

        return await self.update(client)

    async def update_client_balance(self, id: str, balance: float) -> ClientModel:

        client = await self.get_model_by_id(id)
        if client.active is False:
            raise ClientCanNotBeUpdatedError(client_id=id)

        client.balance = float(balance)
        return await self.update(client)

    async def update_client_status(self, id: str, status: bool) -> ClientModel:
        client = await self.get_model_by_id(id)
        if client.active == status:
            raise ClientStatusError(client_id=id)

        client.active = status
        return await self.update(client)

    async def get_all(self) -> List[ClientModel]:
        clients = await self.clients.find().to_list(1000)
        return [ClientModel.from_mongo(client) for client in clients]

    async def create_client(self, name: str, document: str, balance: float) -> ClientModel:
        try:
            new_client = ClientModel(
                name=name,
                document=document,
                balance=balance,
            ).to_mongo()
            result = await self.clients.insert_one(new_client)
            return await self.get_model_by_id(result.inserted_id)
        except Exception as ex:
            LOGGER.error('Error during client creation')
            raise ex
