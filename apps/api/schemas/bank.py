from datetime import datetime
from typing import Optional

from constants.user import UserRole
from pydantic import BaseModel, ConfigDict


class SheduleBase(BaseModel):
    day: int
    start_time: int
    end_time: int
    for_person: bool


class SheduleRead(SheduleBase):
    id: int


class BankBase(BaseModel):
    name: str
    address: str
    city: str
    have_vip: bool
    have_ramp: bool
    have_prime: bool
    lat: float
    lon: float
    for_person: bool
    for_juridical: bool
    schedule: list[SheduleRead]


class BankRead(BankBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class BankList(BaseModel):
    id: int
    name: str
    address: str
    lat: float
    lon: float
    model_config = ConfigDict(from_attributes=True)


class BankListWithRelevance(BankList):
    relevance: float
