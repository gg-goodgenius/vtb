from core.database import get_db
from core.router import generate_router
from dependencies import get_current_active_user, get_current_user
from fastapi import Depends, Query
from schemas import BankList, BankListWithRelevance, BankRead, BankServiceBase, BankServiceRead
from services import (
    count_bank,
    count_service,
    get_all_bank,
    get_all_service,
    get_best_bank,
    get_one_bank,
    get_one_service,
)

router = generate_router(
    get_db=get_db,
    read_schema=BankRead,
    read_list_schema=BankList,
    func_get_one=get_one_bank,
    func_get_all=get_all_bank,
    func_count=count_bank,
    prefix="/bank",
    tags=["Отделения банков"],
)

router_service = generate_router(
    get_db=get_db,
    read_schema=BankServiceRead,
    read_list_schema=BankServiceRead,
    func_get_one=get_one_service,
    func_get_all=get_all_service,
    func_count=count_service,
    prefix="/service",
    tags=["Услуги отделений"],
)


@router.get("/best/", response_model=list[BankListWithRelevance])
def get_best(
    lon: float,
    lat: float,
    service_id: int = 1,
    need_ramp: bool = False,
    need_premium: bool = False,
    radius: float = Query(description="Радиус поиска в километрах"),
    db=Depends(get_db),
):
    return get_best_bank(
        db=db, lon=lon, lat=lat, radius=radius, service_id=service_id, need_ramp=need_ramp, need_premium=need_premium
    )
