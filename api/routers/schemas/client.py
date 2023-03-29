from typing import Optional
from pydantic import BaseModel, root_validator


CLIENT_ID = dict(example='abc123', min_length=24, max_length=24)


class CreateClient(BaseModel):
    name: str
    document: str
    balance: float

class UpdateClientBasicInfo(BaseModel):
    name: Optional[str]
    document: Optional[str]

    @root_validator()
    def require_at_least_one_field(cls, fields):
        assert any([fields['name'], fields['document']]), f'Required at least one field [name, document]'
        return fields

class UpdateClientBalance(BaseModel):
    balance: float

class UpdateClientStatus(BaseModel):
    status: bool

EXAMPLE_CREATE_CLIENT = CreateClient(
    name='client name', 
    document='00000000011',
    balance=123.55
).dict()


EXAMPLE_UPDATE_CLIENT_BASIC_INFO = UpdateClientBasicInfo(
    name='client name', 
    document='00000000011'
).dict()


EXAMPLE_UPDATE_CLIENT_BALANCE = UpdateClientBalance(
    balance=123.55
).dict()


EXAMPLE_UPDATE_CLIENT_STATUS = UpdateClientStatus(
    status=False
).dict()
