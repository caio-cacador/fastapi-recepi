from mongoengine import (StringField, BooleanField, DecimalField)
from api.models.base import BaseDocument
from pydantic import BaseModel
from datetime import datetime

class ClientModel(BaseModel):
    id: str
    name: str
    document: str
    balance: float
    active: bool
    created_at: datetime
    updated_at: datetime


class ClientDocument(BaseDocument):
    meta = {'collection': 'clients'}

    name = StringField(Required=True)
    document = StringField(Required=True)
    balance = DecimalField(default=0)
    active = BooleanField(default=True)

    @property
    def model(self):
        return ClientModel(
            id= str(self.pk),
            name=self.name,
            document=self.document,
            balance=self.balance,
            active=self.active,
            created_at=self.created_at,
            updated_at=self.updated_at
        )
