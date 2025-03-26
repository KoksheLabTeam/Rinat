from typing import Annotated

from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from app.api.depends.user import get_current_user
from app.core.database.helper import get_session
from app.core.models.user import User
from app.core.schemas.order import OrderCreate, OrderUpdate
from app.core.services.order import (
    create_order,
    get_all_orders,
    get_user_order,
    update_order,
)

router = APIRouter(prefix="/order", tags=["Order"])


@router.post("/")
def create_order(
    x_telegram_id: Annotated[str, Header()],
    data: OrderCreate,
    session: Annotated[Session, Depends(get_session)],
):
    return create_order(session, data, x_telegram_id)


@router.get("/")
def get_user_orders(
    x_telegram_id: Annotated[str, Header()],
    session: Annotated[Session, Depends(get_session)],
):
    return get_user_order(session, x_telegram_id)


@router.get("/all")
def get_orders(
    user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return get_all_orders(session)


@router.patch("/{order_id}")
def update_order(
    order_id: int,
    data: OrderUpdate,
    session: Annotated[Session, Depends(get_session)],
):
    return update_order(session, data, order_id)
