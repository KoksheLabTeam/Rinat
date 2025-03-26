from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class Food(Base):
    __tablename__ = "foods"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    photo: Mapped[str] = mapped_column(String(255), nullable=True)
