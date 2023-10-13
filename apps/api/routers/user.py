from core.database import get_db
from core.router import generate_router
from dependencies import get_current_active_user, get_current_user
from fastapi import Depends
from schemas import UserCreate, UserRead, UserReadList, UserUpdate
from services import count_user, create_user, delete_user, get_all_user, get_one_user, update_user

router = generate_router(
    get_db=get_db,
    create_schema=UserCreate,
    read_schema=UserRead,
    read_list_schema=UserReadList,
    update_schema=UserUpdate,
    func_create=create_user,
    func_get_one=get_one_user,
    func_get_all=get_all_user,
    func_update=update_user,
    func_delete=delete_user,
    func_count=count_user,
    prefix="/user",
    tags=["Пользователи"],
)


@router.get("/me/", response_model=UserRead)
def me(current_user: UserRead = Depends(get_current_active_user)):
    print(current_user)
    return current_user
