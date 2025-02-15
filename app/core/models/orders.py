from app.core.models.base import Base

from  sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Table, Column

order_to_food = Table(
    'order_to_food',
    Base.metadata,
    Column("order_id",  ForeignKey("orders.id")),  # Ссылка на таблицу orders
    Column("food_id",  ForeignKey("foods.id"))
)

class Orders(Base):
    __tablename__ = 'orders'
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    datetime: Mapped[str]
    address: Mapped[str]
    full_name: Mapped[str]
    status: Mapped[str]
    phone_number: Mapped[str]
    total_price: Mapped[str]

