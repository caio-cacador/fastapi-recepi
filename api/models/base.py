from datetime import datetime
from typing import Optional
from bson.objectid import ObjectId
from pydantic import BaseModel, validator
from api.utils.date import (
    get_datetime,
    get_isoformat,
    format_all_datetime_to_iso,
    format_all_iso_to_datetime
)


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class MongoModel(BaseModel):
    id: Optional[PyObjectId]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @validator('created_at', always=True)
    def set_created_at(cls, created_at):
        return get_datetime(created_at)

    @validator('updated_at', always=True)
    def set_updated_at(cls, updated_at):
        return get_datetime(updated_at)

    def to_mongo(self) -> dict:
        data = self.__dict__
        if data.get('id') is None:
            data.pop('id', None)        
        data.pop('updated_at', None)
        data = format_all_datetime_to_iso(data)
        return dict(
            data,
            updated_at = get_isoformat()
        )

    @classmethod
    def from_mongo(cls, data: dict):
        if not data:
            return data
        id = data.pop('_id')

        return cls(**dict(
            format_all_iso_to_datetime(data),
            id=str(id),
        ))

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat(),
            ObjectId: lambda oid: str(oid),
        }
    # def mongo(self, **kwargs):
    #     exclude_unset = kwargs.pop('exclude_unset', True)
    #     by_alias = kwargs.pop('by_alias', True)

    #     parsed = self.dict(
    #         exclude_unset=exclude_unset,
    #         by_alias=by_alias,
    #         **kwargs,
    #     )

    #     if '_id' not in parsed and 'id' in parsed:
    #         parsed['_id'] = parsed.pop('id')

    #     return parsed
