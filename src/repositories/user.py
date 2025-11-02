from pydantic import BaseModel, EmailStr
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase

from src.models.users import UsersModel
from src.repositories.base import BaseRepository
from src.schemas.user import User, UserWithHashPassword


class UserRepository(BaseRepository):
    model: DeclarativeBase = UsersModel
    schema: BaseModel = User

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select(self.model).filter_by(email=email)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if not model:
            return None
        return UserWithHashPassword.model_validate(model)

