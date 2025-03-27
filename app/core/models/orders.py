from sqlalchemy import DECIMAL, Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models.base import Base
from app.core.models.mixins.audit import AuditMixin
from app.core.utils.enums import OrderStatus


class Order(Base, AuditMixin):
    __tablename__ = "orders"

    telegram_id: Mapped[str]
    basket_id: Mapped[int] = mapped_column(ForeignKey("baskets.id"))

    address: Mapped[str] = mapped_column(String(255), nullable=False)
    customer_name: Mapped[str] = mapped_column(String(255), nullable=False)
    customer_phone: Mapped[str] = mapped_column(String(20), nullable=False)

    status: Mapped[str] = mapped_column(
        Enum(OrderStatus, name="order_status"),
        default=OrderStatus.PENDING,
        nullable=False,
    )

    total_price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
