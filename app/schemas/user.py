# schemas/user.py
# Schemas to create user, get user or update
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    phone: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    password: Optional[str] = None


class UserResponse(BaseModel):
    phone: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    photo: Optional[str] = None


__all__ = ["UserCreate", "UserUpdate", "UserResponse"]
