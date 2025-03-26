from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base


class User(Base):
    __tablename__ = "users"

    telegram_id: Mapped[str] = mapped_column(unique=True)

    first_name: Mapped[str]
    last_name: Mapped[str]

    is_active: Mapped[bool] = mapped_column(default=True)
    is_staff: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
