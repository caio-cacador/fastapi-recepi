from api.services.logger import LOGGER
from typing import List
from api.models.client import ClientDocument, ClientModel
from api.exceptions.repo_exceptions import ClientCanNotBeUpdatedError, ClientNotFoundError, ClientStatusError


class ClientRepository():

    async def _get_by_id(self, id: str) -> ClientModel:
        client = ClientDocument.objects.get(pk=id)
        if not client:
            raise ClientNotFoundError(client_id=id)
        return client

    async def update_client_personal_info(
        self,
        id: str, 
        name: str = None, 
        document: str = None
      ) -> ClientModel:

        client = await self._get_by_id(id)
        if client['active'] is False:
            raise ClientCanNotBeUpdatedError(client_id=id)

        if name:
            client['name'] = name
        if document:
            client['document'] = document

        client.update_safilly()
        return client.model

    async def update_client_balance(self, id: str, balance: float) -> ClientModel:

        client = await self._get_by_id(id)
        if client.active is False:
            raise ClientCanNotBeUpdatedError(client_id=id)

        client.balance = float(balance)

        client.update_safilly()
        return client.model

    async def update_client_status(self, id: str, status: bool) -> ClientModel:
        client = await self._get_by_id(id)
        if client.active == status:
            raise ClientStatusError(client_id=id)

        client.active = status

        client.update_safilly()
        return client.model

    async def get_all(self) -> List[ClientModel]:
        clients = ClientDocument.objects().all()
        return [client.model for client in clients]

    async def get_model_by_id(self, id: str) -> ClientModel:
        client = await self._get_by_id(id)
        return client.model

    async def create_client(self, name: str, document: str, balance: float) -> ClientModel:
        try:
            new_client = ClientDocument(
                name=name,
                document=document,
                balance=balance,
            )
            new_client.save()
            return new_client.model
        except Exception as ex:
            LOGGER.error('Error during client creation')
            raise ex
