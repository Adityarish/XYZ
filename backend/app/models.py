# models.py
from pydantic import BaseModel, Field, ConfigDict, BeforeValidator
from typing import Optional, Annotated
from bson import ObjectId

# Represents an ObjectId field in the database.
# It will be validated as a string.
PyObjectId = Annotated[str, BeforeValidator(str)]

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

class TodoInDB(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    completed: bool

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
