from typing import Optional

from app.core.schemas.base import BaseSchema




class OrderCreate(BaseSchema):
    user_id: int
    datetime: int
    address: str
    full_name: str
    status: str
    phone_number: str
    total_price: float


class OrderRead(BaseSchema):
    datetime: int
    address: str
    full_name: str
    status: str
    phone_number: str
    total_price: float


class OrderUpdate(BaseSchema):
    datetime: Optional[int] = None
    address: Optional[str] = None
    full_name: Optional[str] = None
    status: Optional[str] = None
    phone_number: Optional[str] = None
    total_price: Optional[bool] = None



