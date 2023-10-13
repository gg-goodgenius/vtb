from datetime import datetime

from fastapi.param_functions import Form
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
from schemas.user import UserCreate, UserRead


class SignUp(UserCreate):
    pass


class SignIn(OAuth2PasswordRequestForm):
    def __init__(
        self,
        username: str = Form(description="Enter email address"),
        password: str = Form(),
    ):
        self.email = username
        self.password = password


class Token(BaseModel):
    access_token: str
    access_token_expired_at: datetime
    token_type: str
    refresh_token: str
    refresh_token_expired_at: datetime
    user: UserRead
