from typing import Optional

from app.core.schemas.base import BaseSchema
from app.core.utils.enums import OrderStatus


class OrderRead(BaseSchema):
    id: int
    user_id: int
    address: str
    customer_name: str
    customer_phone: str

    status: str
    total_price: float


class OrderCreate(BaseSchema):
    address: str
    customer_name: str
    customer_phone: str


class OrderUpdate(BaseSchema):
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None

    status: Optional[OrderStatus] = None
