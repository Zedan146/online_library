from pydantic import BaseModel


class Role(BaseModel):
    id: int
    title: str


class RoleAdd(BaseModel):
    title: str
