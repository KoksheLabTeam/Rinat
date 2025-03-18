from typing import Annotated
from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import Session

from app.core.models.food import 