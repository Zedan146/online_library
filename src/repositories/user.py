from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase

from src.models.users import UsersModel
from src.repositories.base import BaseRepository
from src.schemas.user import User


class UserRepository(BaseRepository):
    model: DeclarativeBase = UsersModel
    schema: BaseModel = User


