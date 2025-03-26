from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, joinedload

from app.core.models.basket import Basket
from app.core.models.orders import Order
from app.core.schemas.order import OrderCreate, OrderUpdate


def create_order(session: Session, data: OrderCreate, telegram_id: str) -> Order:
    basket = session.query(Basket).filter_by(telegram_id=telegram_id).first()

    if not basket:
        raise HTTPException(status_code=404, detail="Корзина не найдена")

    order = Order(
        **data.model_dump(),
        basket_id=basket.id,
        telegram_id=telegram_id,
    )

    try:
        session.add(order)
        session.commit()
        session.refresh(order)
        return order

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных.",
        )


def get_user_order(session: Session, telegram_id: str):
    orders = (
        session.query(Order)
        .options(joinedload(Order.basket).joinedload(Basket.foods))
        .filter(Order.telegram_id == telegram_id)
        .all()
    )

    if not orders:
        raise HTTPException(status_code=404, detail="Заказы не найдены")

    return [
        {
            "id": order.id,
            "address": order.address,
            "customer_name": order.customer_name,
            "customer_phone": order.customer_phone,
            "status": order.status,
            "total_price": order.total_price,
            "foods": [
                {
                    "id": food.id,
                    "name": food.name,
                    "price": food.price,
                    "description": food.description,
                    "photo": food.photo,
                }
                for food in order.basket.foods
            ],
        }
        for order in orders
    ]


def get_all_orders(session: Session):
    orders = (
        session.query(Order)
        .options(joinedload(Order.basket).joinedload(Basket.foods))
        .all()
    )

    return [
        {
            "id": order.id,
            "telegram_id": order.telegram_id,
            "address": order.address,
            "customer_name": order.customer_name,
            "customer_phone": order.customer_phone,
            "status": order.status,
            "total_price": order.total_price,
            "foods": [
                {
                    "id": food.id,
                    "name": food.name,
                    "price": food.price,
                    "description": food.description,
                    "photo": food.photo,
                }
                for food in order.basket.foods
            ],
        }
        for order in orders
    ]


def update_order(session: Session, data: OrderUpdate, order_id: int):
    order = session.query(Order).where(Order.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")

    update_data = data.model_dump(exclude_none=True, exclude_unset=True)

    for key, value in update_data.items():
        setattr(order, key, value)

    try:
        session.commit()
        session.refresh(order)
        return order

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных.",
        )
