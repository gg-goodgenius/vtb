from core.database import get_db
from core.router import generate_router
from dependencies import get_current_active_user, get_current_user
from fastapi import Depends, Query
from schemas import BankListWithRelevance, BankRead
from services import count_bank, get_all_bank, get_best_bank, get_one_bank

router = generate_router(
    get_db=get_db,
    read_schema=BankRead,
    read_list_schema=BankListWithRelevance,
    func_get_one=get_one_bank,
    func_get_all=get_all_bank,
    func_count=count_bank,
    prefix="/bank",
    tags=["Отделения банков"],
)


@router.get("/best/", response_model=list[BankListWithRelevance])
def get_best(
    lon: float, lat: float, radius: float = Query(description="Радиус поиска в километрах"), db=Depends(get_db)
):
    return get_best_bank(db=db, lon=lon, lat=lat, radius=radius)
