from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    # @classmethod
    # def __modify_schema__(cls, field_schema):
    #     field_schema.update(type="string")


class TaskModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str = Field(...)
    description: str = Field(...)
    done: bool = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "Title": "Task_title",
                "description": "Task_description",
                "done": "Task status",
            }
        }


class UpdateTaskModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    done: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "Title": "Task_title",
                "description": "Task_description",
                "done": "Task status",
            }
        }
