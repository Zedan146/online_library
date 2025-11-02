from pydantic import BaseModel, ConfigDict


class Role(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


class RoleAdd(BaseModel):
    title: str
