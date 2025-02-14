from app.core.models.base import Base

from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str] = mapped_column(nullable=True)

    is_active: Mapped[bool] = mapped_column(default=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
