from typing import Annotated

from fastapi import APIRouter, Depends

from app.api.depends.user import get_current_user
from app.core.models.user import User
from app.core.schemas.user import UserRead

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", response_model=UserRead)
def get_me(user: Annotated[User, Depends(get_current_user)]):
    return user
