from constants import ALGORITHM, SECRET_KEY, UserRole, oauth2_scheme
from core.database import get_db
from exceptions import InvalidCredentials, PermissionDenied, TokenExpired, UserIsNotActive
from fastapi import Depends
from jose import JWTError, jwt
from models import User
from schemas import UserRead
from services import get_one_user
from sqlalchemy.orm import Session


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserRead:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("sub"))
        if user_id is None or payload.get("type") != "access":
            raise InvalidCredentials
    except JWTError as err:
        raise TokenExpired
    user = get_one_user(db=db, id=user_id)
    if user is None:
        raise InvalidCredentials
    return user


def get_current_user_from_refresh_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> UserRead:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("sub"))
    except JWTError as err:
        raise TokenExpired
    user = get_one_user(db=db, id=user_id)
    if user is None:
        raise InvalidCredentials
    return user


def get_current_active_user(current_user: UserRead = Depends(get_current_user)):
    if not current_user.is_active:
        raise UserIsNotActive
    return current_user


def get_user_with_required_roles(roles: list[UserRole]):
    def have_roles(current_active_user: UserRead = Depends(get_current_active_user)):
        if current_active_user.role not in roles:
            raise PermissionDenied
        return current_active_user

    return have_roles
