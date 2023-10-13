from typing import Optional

from constants import UserRole
from core.database import Base
from core.schema import BoolResult, Pagination
from dependencies import get_user_with_required_roles
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from schemas import UserRead
from sqlalchemy import select
from sqlalchemy.orm import Session


def generate_router(
    get_db,
    create_schema=None,
    read_schema=None,
    read_list_schema=None,
    update_schema=None,
    func_create=None,
    func_get_one=None,
    func_get_all=None,
    func_update=None,
    func_delete=None,
    func_count=None,
    user_role: UserRole = UserRole.OPERATOR,
    prefix: str = "",
    tags: list = [],
):
    router = APIRouter(prefix=prefix, tags=tags)
    if func_create:

        @router.post("/", response_model=read_schema)
        def route_create(
            create: create_schema,
            db: Session = Depends(get_db),
            # current_user: UserRead = Depends(get_user_with_required_roles(roles=[user_role])),
        ) -> read_schema:
            return func_create(db=db, create=create)

    if func_get_all:

        @router.get("/", response_model=list[read_list_schema])
        def route_get_all(
            db: Session = Depends(get_db),
            pagination: Pagination = Depends(Pagination),
            # current_user: UserRead = Depends(get_user_with_required_roles(roles=[user_role])),
        ) -> list[read_list_schema]:
            return func_get_all(db=db, offset=pagination.offset, limit=pagination.limit)

    if func_get_one:

        @router.get("/{id}", response_model=read_schema)
        def route_get_one(
            id: int,
            db: Session = Depends(get_db),
            # current_user: UserRead = Depends(get_user_with_required_roles(roles=[user_role])),
        ) -> read_schema:
            return func_get_one(db=db, id=id)

    if func_count:

        @router.get("/count/", response_model=int)
        def route_count(
            db: Session = Depends(get_db),
            # current_user: UserRead = Depends(get_user_with_required_roles(roles=[user_role])),
        ) -> int:
            return func_count(db=db)

    if func_update:

        @router.patch("/{id}", response_model=read_schema)
        def route_update(
            id: int,
            update: update_schema,
            db: Session = Depends(get_db),
            # current_user: UserRead = Depends(get_user_with_required_roles(roles=[user_role])),
        ) -> read_schema:
            print(update)
            return func_update(db=db, id=id, update=update)

    if func_delete:

        @router.delete("/{id}", response_model=BoolResult)
        def route_delete(
            id: int,
            db: Session = Depends(get_db),
            # current_user: UserRead = Depends(get_user_with_required_roles(roles=[user_role])),
        ) -> BoolResult:
            return func_delete(db=db, id=id)

    return router
