from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.models.basket import Basket, basket_food
from app.core.models.food import Food


def create_basket(session: Session, telegram_id: str) -> Basket:
    basket = Basket(telegram_id=telegram_id)

    try:
        session.add(basket)
        session.commit()
        session.refresh(basket)
        return basket

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных.",
        )


def add_food(session: Session, telegram_id: str, food_id: int):
    basket = session.query(Basket).filter_by(telegram_id=telegram_id).first()
    if not basket:
        basket = create_basket(session, telegram_id)

    food = session.query(Food).filter_by(id=food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Товар не найден")

    stmt = basket_food.select().where(
        (basket_food.c.basket_id == basket.id) & (basket_food.c.food_id == food.id)
    )
    existing_item = session.execute(stmt).fetchone()

    if existing_item:
        raise HTTPException(status_code=400, detail="Товар уже в корзине")

    session.execute(basket_food.insert().values(basket_id=basket.id, food_id=food_id))

    try:
        session.commit()
        return {"message": "Товар добавлен в корзину"}
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных",
        )


def remove_food(session: Session, telegram_id: str, food_id: int):
    basket = session.query(Basket).filter_by(telegram_id=telegram_id).first()

    if not basket:
        raise HTTPException(status_code=404, detail="Корзина не найдена")

    food = session.query(Food).filter_by(id=food_id).first()

    if not food:
        raise HTTPException(status_code=404, detail="Товар не найден")

    session.execute(
        basket_food.delete().where(
            (basket_food.c.basket_id == basket.id) & (basket_food.c.food_id == food.id)
        )
    )

    try:
        session.commit()
        return {"message": "Товар удален из корзины"}
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных",
        )


def get_basket(session: Session, telegram_id: str):
    basket = session.query(Basket).filter_by(telegram_id=telegram_id)

    try:
        result = session.execute(basket)
        return result.scalar_one_or_none()

    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных",
        )
