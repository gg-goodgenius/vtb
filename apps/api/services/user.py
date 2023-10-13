from constants import PWD_CONTEXT
from core.service import generate_services
from fastapi import HTTPException, status
from models import User
from pydantic import EmailStr
from schemas import UserCreate, UserRead, UserReadList, UserUpdate
from sqlalchemy.orm import Session

(
    _,
    get_one_user,
    get_all_user,
    find_one_user,
    find_all_user,
    update_user,
    delete_user,
    count_user,
) = generate_services(
    db_model=User,
    create_schema=UserCreate,
    read_schema=UserRead,
    read_list_schema=UserReadList,
    update_schema=UserUpdate,
)


def get_one_user_by_email(db: Session, email: EmailStr) -> UserRead | None:
    try:
        result: UserRead | None = db.query(User).filter(User.email == email).first()
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
    return result


def create_user(db: Session, create: UserCreate) -> UserRead:
    try:
        d_user = create.model_dump()
        d_user["hashed_password"] = PWD_CONTEXT.hash(create.password)
        d_user["is_active"] = False
        del d_user["password"]
        db_user = User(**d_user)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
    return db_user
