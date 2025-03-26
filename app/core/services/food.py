from typing import List

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.models.food import Food
from app.core.schemas.food import FoodCreate


def create_food(session: Session, data: FoodCreate) -> Food:
    food = Food(**data.model_dump())

    try:
        session.add(food)
        session.commit()
        session.refresh(food)
        return food

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных.",
        )


def get_all_foods(session: Session) -> List[Food]:
    statement = select(Food)

    try:
        result = session.execute(statement)
        return result.scalars().all()

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка базы данных.",
        )
