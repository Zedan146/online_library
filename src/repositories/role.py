from pydantic import BaseModel

from src.models import RolesModel
from src.repositories.base import BaseRepository
from src.schemas.role import Role


class RoleRepository(BaseRepository):
    model = RolesModel
    schema: BaseModel = Role


