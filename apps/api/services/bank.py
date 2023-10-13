from math import exp, sqrt

from constants import PWD_CONTEXT
from core.service import generate_services
from fastapi import HTTPException, Query, status
from models import Bank
from pydantic import EmailStr
from schemas import BankBase, BankList, BankListWithRelevance, BankRead
from sqlalchemy import select
from sqlalchemy.orm import Session

(
    _,
    get_one_bank,
    get_all_bank,
    _,
    _,
    _,
    _,
    count_bank,
) = generate_services(
    db_model=Bank,
    create_schema=BankBase,
    read_schema=BankRead,
    read_list_schema=BankList,
    update_schema=BankBase,
)


def _get_distance(x1: float, x2: float, y1: float, y2: float) -> float:
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 111


def get_best_bank(db: Session, lon: float, lat: float, radius: float) -> list[BankListWithRelevance]:
    radius_degree: float = radius / 111
    try:
        bank_instances = (
            db.query(Bank)
            .where(
                Bank.lat < lat + radius_degree,
                Bank.lat > lat - radius_degree,
                Bank.lon < lon + radius_degree,
                Bank.lon > lon - radius_degree,
            )
            .all()
        )
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(error))
    distances = list()
    if len(bank_instances) == 0:
        return []
    if len(bank_instances) == 1:
        return BankListWithRelevance(**bank_instances[0].__dict__, relevance=1.0)
    for bank_instance in bank_instances:
        distances.append(
            {
                "bank": bank_instance.__dict__,
                "distance": _get_distance(x1=lon, x2=bank_instance.lon, y1=lat, y2=bank_instance.lat),
            }
        )

    max_distance = max(distances, key=lambda x: x["distance"])["distance"]
    min_distance = min(distances, key=lambda x: x["distance"])["distance"]
    diff_distance = max_distance - min_distance
    result = list(
        map(
            lambda dist: BankListWithRelevance(
                **dist["bank"], relevance=1 - (dist["distance"] - min_distance) / diff_distance
            ),
            distances,
        )
    )
    result.sort(reverse=True, key=lambda x: x.relevance)
    return result[:10]
