from datetime import datetime, timezone
from typing import TYPE_CHECKING, List

from sqlalchemy import Column, DateTime, ForeignKey, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models.base import Base

if TYPE_CHECKING:
    from app.core.models.food import Food

basket_food = Table(
    "basket_food",
    Base.metadata,
    Column("basket_id", ForeignKey("baskets.id"), primary_key=True),
    Column("food_id", ForeignKey("foods.id"), primary_key=True),
    Column("added_at", DateTime, default=datetime.now(timezone.utc), nullable=False),
)


class Basket(Base):
    __tablename__ = "baskets"
    telegram_id: Mapped[str] = mapped_column(unique=True)

    foods: Mapped[List["Food"]] = relationship(secondary=basket_food)
