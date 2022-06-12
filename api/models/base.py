from abc import abstractproperty
from datetime import datetime
from mongoengine import (
    DateTimeField,
    Document
)

class BaseDocument(Document):
    meta = {'abstract': True}

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    @abstractproperty
    def model(self):
        pass

    def update_safilly(self):
        self.updated_at = datetime.utcnow()
        return super().save()

