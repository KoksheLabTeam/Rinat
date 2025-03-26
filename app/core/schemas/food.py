from typing import Optional

from app.core.schemas.base import BaseSchema


class FoodRead(BaseSchema):
    id: int
    name: str
    price: int
    description: Optional[str] = None
    photo: Optional[str] = None


class FoodCreate(BaseSchema):
    name: str
    price: int
    description: Optional[str] = None


class FoodUpdate(BaseSchema):
    name: Optional[str] = None
    price: Optional[bool] = None
    description: Optional[str] = None
