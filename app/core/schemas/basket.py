from typing import List

from app.core.schemas.base import BaseSchema
from app.core.schemas.food import FoodRead


class BasketRead(BaseSchema):
    foods: List[FoodRead]
