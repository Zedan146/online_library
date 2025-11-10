from pydantic import BaseModel, EmailStr, ConfigDict

from src.schemas.mixin import NonEmptyStringMixin


class UserLogin(NonEmptyStringMixin):
    email: EmailStr
    password: str


class UserRequestAdd(UserLogin):
    username: str
    first_name: str
    last_name: str


class UserAdd(NonEmptyStringMixin):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    role_id: int
    hashed_password: str


class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    role_id: int

    model_config = ConfigDict(from_attributes=True)


class UserWithHashPassword(User):
    hashed_password: str
