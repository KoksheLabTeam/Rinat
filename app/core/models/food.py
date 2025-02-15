from app.core.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column


class Foods(Base):
    __tablename__ = 'foods'
    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]
    photo: Mapped[str] = mapped_column(nullable=True)
