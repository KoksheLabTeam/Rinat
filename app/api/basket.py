from typing import Annotated

from fastapi import APIRouter, Depends, Header, status
from sqlalchemy.orm import Session

from app.core.database.helper import get_session
from app.core.schemas.basket import BasketRead
from app.core.services import basket as basket_service

router = APIRouter(prefix="/basket", tags=["Basket"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_food(
    food_id: int,
    x_telegram_id: Annotated[str, Header()],
    session: Annotated[Session, Depends(get_session)],
):
    return basket_service.add_food(session, x_telegram_id, food_id)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def remove_food(
    food_id: int,
    x_telegram_id: Annotated[str, Header()],
    session: Annotated[Session, Depends(get_session)],
):
    return basket_service.remove_food(session, x_telegram_id, food_id)


@router.get("/", response_model=BasketRead)
def get_user_basket(
    x_telegram_id: Annotated[str, Header()],
    session: Annotated[Session, Depends(get_session)],
):
    return basket_service.get_basket(session, x_telegram_id)
