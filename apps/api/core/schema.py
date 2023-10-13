from pydantic import BaseModel


class BoolResult(BaseModel):
    result: bool


class Pagination(BaseModel):
    offset: int = 0
    limit: int = 10
