from typing import Optional

from core.database import Base
from core.schema import BoolResult
from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session


def generate_services(
    db_model: Base,
    create_schema,
    read_schema,
    read_list_schema,
    update_schema,
):
    def get_one(db: Session, id: int) -> read_schema:
        try:
            result = db.query(db_model).filter(db_model.id == id).first()
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
        return result

    def get_all(db: Session, offset: int = 0, limit: int = 10) -> list[read_list_schema]:
        try:
            result = db.query(db_model).offset(offset).limit(limit).all()
        except Exception as err:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
        return result

    def create(db: Session, create: create_schema) -> read_schema:
        try:
            db_instance = db_model(**create.model_dump())
            db.add(db_instance)
            db.commit()
            db.refresh(db_instance)
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
        return db_instance

    def count(db: Session) -> int:
        try:
            result = db.query(db_model.id).count()
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
        return result

    def update(db: Session, id: int, update: update_schema) -> read_schema:
        try:
            db_instance: db_model = get_one(db=db, id=id)
            if not db_instance:
                raise HTTPException(status_code=404, detail="Record not found")
            update_data = update.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_instance, key, value)
            db.add(db_instance)
            db.commit()
            db.refresh(db_instance)
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
        return db_instance

    def find_one(db: Session, defualt: dict) -> read_schema:
        try:
            statements = list()
            for key in list(defualt.keys()):
                statements.append(getattr(db_model, key) == defualt.get(key, None))
            result = db.query(db_model).where(*statements)
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
        return result.first()

    def find_all(db: Session, defualt: dict) -> list[read_list_schema]:
        try:
            statements = list()
            for key in list(defualt.keys()):
                statements.append(getattr(db_model, key) == defualt.get(key, None))
            result = db.query(db_model).where(*statements)
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
        return result.all()

    def delete(db: Session, id: int) -> BoolResult:
        try:
            db_instance = get_one(db=db, id=id)
            if not db_instance:
                raise HTTPException(status_code=404, detail="Record not found")
            db.delete(db_instance)
            db.commit()
        except Exception as error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
        return BoolResult(result=True)

    return (create, get_one, get_all, find_one, find_all, update, delete, count)
