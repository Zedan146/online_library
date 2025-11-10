from enum import Enum

from pydantic import BaseModel, ConfigDict


class RoleName(str, Enum):
    ADMIN = "admin"
    AUTHOR = "author"
    USER = "user"


class RoleAdd(BaseModel):
    title: RoleName


class Role(RoleAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)
