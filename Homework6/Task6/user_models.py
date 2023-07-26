from pydantic import BaseModel, Field, EmailStr
from settings import settings


class UserIn(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    last_name: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    email: EmailStr = Field(..., max_length=settings.EMAIL_MAX_LENGTH)
    password: str = Field(..., max_length=settings.EMAIL_MAX_LENGTH)


class UserUpdate(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    last_name: str = Field(..., min_length=2, max_length=settings.NAME_MAX_LENGTH)
    email: EmailStr = Field(..., max_length=settings.EMAIL_MAX_LENGTH)


class User(UserUpdate):
    id: int
