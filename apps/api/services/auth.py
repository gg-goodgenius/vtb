from datetime import datetime, timedelta
from uuid import uuid4

from constants import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    PWD_CONTEXT,
    REFRESH_TOKEN_EXPIRE_MINUTES,
    SECRET_KEY,
    UserRole,
)
from exceptions import InvalidCredentials, UserIsNotActive, UserNotExist, VerifyError
from jose import jwt
from models import User
from pydantic import EmailStr
from schemas import SignIn, SignUp, Token, UserCreate, UserRead
from services.user import create_user, get_one_user_by_email
from sqlalchemy.orm import Session


def _verify_password(plain_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def _authenticate(email: EmailStr, password: str, db: Session):
    user = get_one_user_by_email(db=db, email=email)
    if user is None:
        raise UserNotExist
    else:
        if not _verify_password(password, user.hashed_password):
            raise InvalidCredentials
    if not user.is_active:
        raise UserIsNotActive
    return user


def _create_access_token(subject: int, expires_delta: timedelta | None = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject), "type": "access"}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def _create_refresh_token(subject: int, expires_delta: timedelta | None = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": str(subject), "type": "refresh"}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def signup(data: SignUp, db: Session) -> UserRead:
    schema_user_create = UserCreate(
        **(data.model_dump()),
    )
    new_user = create_user(create=schema_user_create, db=db)
    return new_user


def signin(data: SignIn, db: Session) -> Token:
    user = _authenticate(email=data.email, password=data.password, db=db)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    access_token = _create_access_token(user.id, expires_delta=access_token_expires)
    refresh_token = _create_refresh_token(user.id, expires_delta=refresh_token_expires)
    return Token(
        access_token=access_token,
        access_token_expired_at=datetime.utcnow() + access_token_expires,
        token_type="bearer",
        refresh_token=refresh_token,
        refresh_token_expired_at=datetime.utcnow() + refresh_token_expires,
        user=user,
    )


def update_access_refresh_tokens(user: UserRead) -> Token:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    access_token = _create_access_token(user.id, expires_delta=access_token_expires)
    refresh_token = _create_refresh_token(user.id, expires_delta=refresh_token_expires)
    return Token(
        access_token=access_token,
        access_token_expired_at=datetime.utcnow() + access_token_expires,
        token_type="bearer",
        refresh_token=refresh_token,
        refresh_token_expired_at=datetime.utcnow() + refresh_token_expires,
        user=user,
    )
