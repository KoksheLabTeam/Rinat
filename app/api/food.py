from typing import Annotated
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import current_user
from sqlalchemy.testing.suite.test_reflection import users

from app.core.models.food import Foods
from app.core.services import food as food_service
from app.core.schemas.food import FoodCreate,FoodRead,FoodUpdate

from app.core.database.helper import get_session
from app.api.depends.user import get_current_user , get_admin_user

from app.core.models.user import User


router = APIRouter(prefix="/food", tags=["food"])

@router.post("/", response_model=FoodRead)
def create_food(
     data: FoodCreate,
     admin_user: Annotated[User,Depends(get_admin_user)],
     session:Annotated[Session,Depends(get_session)],
):

    return food_service.get_all_foods(session)

@router.get("/", response_model= list[FoodRead])
def get_all_foods(

        session:Annotated[Session,Depends(get_session)],

):
    return food_service.get_all_foods(session)

@router.patch("/{id}", response_model=FoodRead)
def update_food_by_id(
        id: int,
        data: FoodUpdate,
        admin_user: Annotated[User,Depends(get_admin_user)],
        session:Annotated[Session,Depends(get_session)],

):

    return food_service.update_food_by_id(session=session, data=data, todo_id=id)

@router.delete("/{id}", response_model=FoodRead)
def delete_food_by_id(
        id: int,
        admin_user: Annotated[User,Depends(get_admin_user)],
        session:Annotated[Session,Depends(get_session)],
):
    return food_service.delete_food_by_id(session=session, id=id)

@router.get("/{id}", response_model=FoodRead)
def get_food_by_id(
        id: int,
        admin_user: Annotated[User, Depends(get_admin_user)],
        session:Annotated[Session,Depends(get_session)],
):
    return food_service.get_food_by_id_for_user(
        session=session,
        food_id=id,
        user_id=current_user.id
    )
