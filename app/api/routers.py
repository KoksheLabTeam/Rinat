from fastapi import APIRouter

from .basket import router as basket_router
from .food import router as food_router
from .order import router as order_router
from .user import router as user_router

routers = APIRouter(prefix="/api")

routers.include_router(user_router)
routers.include_router(food_router)
routers.include_router(basket_router)
routers.include_router(order_router)
