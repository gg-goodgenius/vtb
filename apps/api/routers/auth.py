from constants import oauth2_scheme
from core.database import get_db
from dependencies import get_current_active_user, get_current_user_from_refresh_token
from fastapi import APIRouter, Depends, HTTPException, Query
from schemas import SignIn, SignUp, Token, UserCreate, UserRead
from services import signin, signup, update_access_refresh_tokens

router = APIRouter(prefix="/auth", tags=["Аутентификация и регистрация"])


@router.post("/signup", response_model=UserRead)
def route_signup(data: SignUp, db=Depends(get_db)):
    return signup(data=data, db=db)


@router.post("/signin", response_model=Token)
def route_signin(data: SignIn = Depends(), db=Depends(get_db)):
    return signin(data=data, db=db)


@router.post("/update_token", response_model=Token)
def route_update_tokens(current_active_user=Depends(get_current_user_from_refresh_token), db=Depends(get_db)):
    return update_access_refresh_tokens(user=current_active_user)
