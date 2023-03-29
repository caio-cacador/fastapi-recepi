from api.services.logger import LOGGER
from typing import List
from fastapi import APIRouter, Path, Body, Depends
from api.models.client import ClientModel
from api.repositories.client_repository import ClientRepository
from api.routers.schemas.client import *

router = APIRouter(prefix='/clients', tags=['Clients'])


@router.get("/list", status_code=200, response_model=List[ClientModel])
async def list_all_clients(
        *, client_repo: ClientRepository = Depends(ClientRepository) 
    ) -> List[dict]:
    """
    List all clients in database
    """
    clients = await client_repo.get_all()
    return clients


@router.get("/{client_id}", status_code=200, response_model=ClientModel)
async def get_client_by_id(
        *, 
        client_id: str = Path(**CLIENT_ID),
        client_repo: ClientRepository = Depends(ClientRepository)
    ) -> dict:
    """
    Get Client by ID
    """
    result = await client_repo.get_model_by_id(client_id)
    return result


@router.put("/create", status_code=201, response_model=ClientModel)
async def create_new_client(
        *, 
        new_client: CreateClient = Body(example=EXAMPLE_CREATE_CLIENT),
        client_repo: ClientRepository = Depends(ClientRepository)
    ) -> dict:
    """
    Create a Client
    """
    return await client_repo.create_client(**new_client.dict())

@router.patch("/update/personal_info/{client_id}", status_code=200, response_model=ClientModel)
async def update_personal_info(
        *, 
        client_id: str = Path(**CLIENT_ID),
        info: UpdateClientBasicInfo = Body(example=EXAMPLE_UPDATE_CLIENT_BASIC_INFO),
        client_repo: ClientRepository = Depends(ClientRepository)
    ) -> dict:
    """
    Update a Client personal infomation
    """
    updated_client = await client_repo.update_client_personal_info(id=client_id, **info.dict())
    return updated_client


@router.patch("/update/balance/{client_id}", status_code=200, response_model=ClientModel)
async def update_balance(
        *, 
        client_id: str = Path(**CLIENT_ID),
        data: UpdateClientBalance = Body(example=EXAMPLE_UPDATE_CLIENT_BALANCE),
        client_repo: ClientRepository = Depends(ClientRepository)
    ) -> dict:
    """
    Update a Client balance
    """
    updated_client = await client_repo.update_client_balance(id=client_id, **data.dict())
    return updated_client


@router.patch("/update/status/{client_id}", status_code=200, response_model=ClientModel)
async def update_status(
        *, 
        client_id: str = Path(**CLIENT_ID),
        data: UpdateClientStatus = Body(example=EXAMPLE_UPDATE_CLIENT_STATUS),
        client_repo: ClientRepository = Depends(ClientRepository)
    ) -> dict:
    """
    Update a Client status
    """
    updated_client = await client_repo.update_client_status(id=client_id, **data.dict())
    return updated_client
