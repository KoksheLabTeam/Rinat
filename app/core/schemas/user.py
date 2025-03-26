from app.core.schemas.base import BaseSchema


class UserRead(BaseSchema):
    id: int

    first_name: str
    last_name: str

    is_active: bool
    is_staff: bool
    is_superuser: bool
