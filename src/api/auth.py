from fastapi import APIRouter, Response

from src.database import async_session_maker
from src.exeptions import EmailNotRegisteredHTTPException, IncorrectPasswordHTTPException
from src.repositories.user import UserRepository
from src.schemas.user import UserRequestAdd, UserAdd, UserLogin
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.post("/register", summary="Регистрация пользователя")
async def register_user(data: UserRequestAdd):
    hashed_password = AuthService().get_hashed_password(data.password)
    new_user_data = UserAdd(**data.model_dump(), hashed_password=hashed_password)
    async with async_session_maker() as session:
        await UserRepository(session).add(new_user_data)
        await session.commit()

    return {"status": "OK"}


@router.post("/login", summary="Авторизация пользователя")
async def login_user(data: UserLogin, response: Response):
    async with async_session_maker() as session:
        user = await UserRepository(session).get_user_with_hashed_password(email=data.email)
        if not user:
            raise EmailNotRegisteredHTTPException
        if not AuthService().verify_password(data.password, user.hashed_password):
            raise IncorrectPasswordHTTPException
        access_token = AuthService().create_access_token({"user_id": user.id, "role_id": user.role_id})
        response.set_cookie("access_token", access_token)

        await session.commit()

    return {"message": "Вы успешно авторизовались", "access_token": access_token}

