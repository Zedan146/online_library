from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase

from src.models import RolesModel
from src.repositories.base import BaseRepository
from src.schemas.role import Role


class RoleRepository(BaseRepository):
    model: DeclarativeBase = RolesModel
    schema: BaseModel = Role


