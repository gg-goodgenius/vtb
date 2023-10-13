from datetime import datetime
from typing import Optional

from constants.user import UserRole
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str
    role: UserRole


class UserWithOutRoleCreate(BaseModel):
    username: str
    email: str
    password: str


class UserCreate(UserBase):
    password: str


class UserReadShort(UserBase):
    id: int
    is_active: bool
    model_config = ConfigDict(from_attributes=True)


class UserRead(UserBase):
    id: int
    is_active: bool
    hashed_password: str
    model_config = ConfigDict(from_attributes=True)


class UserReadList(BaseModel):
    id: int
    username: str
    is_active: bool
    email: str
    role: str
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None
