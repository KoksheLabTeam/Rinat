from fastapi import APIRouter

from .user import router as user_router
from .food import router as food_router
from ..bot.main import router

routers = APIRouter(prefix="/api")

routers.include_router(user_router)
routers.include_router(food_router)
