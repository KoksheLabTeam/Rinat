from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depends.user import get_current_user
from app.core.database.helper import get_session
from app.core.models.user import User
from app.core.schemas.food import FoodCreate, FoodRead
from app.core.services import food as food_service

router = APIRouter(prefix="/food", tags=["Food"])


@router.post("/", response_model=FoodRead)
def create_food(
    data: FoodCreate,
    # user: Annotated[User, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_session)],
):
    return food_service.create_food(session, data)


@router.get("/", response_model=list[FoodRead])
def get_all_foods(session: Annotated[Session, Depends(get_session)]):
    return food_service.get_all_foods(session)
