from api.models.base import MongoModel
from typing import Optional
from pydantic import Field


class ClientModel(MongoModel):
    name: str = Field(...)
    document: str = Field(...)
    balance: float = Field(...)
    active: Optional[bool] = Field(True)
