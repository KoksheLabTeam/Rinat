from typing import Annotated

from fastapi import Depends, Header, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.core.database.helper import get_session
from app.core.models.user import User


def get_current_user(
    x_telegram_id: Annotated[str, Header()],
    session: Annotated[Session, Depends(get_session)],
) -> User:

    if not x_telegram_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="x-telegram-id is missing",
        )

    user = (
        session.query(User)
        .filter(User.telegram_id == x_telegram_id, User.is_active == True)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found or inactive.",
        )

    return user
