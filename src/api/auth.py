from fastapi import APIRouter, Response, HTTPException, Request

from sqlalchemy.exc import IntegrityError

from src.api.dep import UserIdDep, DBDep
from src.exeptions import EmailNotRegisteredHTTPException, IncorrectPasswordHTTPException
from src.schemas.role import RoleName
from src.schemas.user import UserRequestAdd, UserAdd, UserLogin
from src.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["Авторизация и аутентификация"])


@router.post("/register", summary="Регистрация пользователя")
async def register_user(data: UserRequestAdd, db: DBDep):
    user_role = await db.roles.get_one_or_none(title=RoleName.USER)
    hashed_password = AuthService().get_hashed_password(data.password)
    new_user_data = UserAdd(**data.model_dump(), role_id=user_role.id, hashed_password=hashed_password)
    try:
        await db.users.add(new_user_data)
        await db.commit()
    except IntegrityError as ex:
        original_error = ex.orig
        error_msg = str(original_error)
        if "ix_users_username" in error_msg:
            raise HTTPException(status_code=409, detail="Пользователь с таким username уже зарегистрирован")
        if "ix_users_email" in error_msg:
            raise HTTPException(status_code=409, detail="Пользователь с таким email уже зарегистрирован")

    return {"status": "OK"}


@router.post("/login", summary="Авторизация пользователя")
async def login_user(data: UserLogin, response: Response, request: Request, db: DBDep):
    if request.cookies.get("access_token"):
        raise HTTPException(status_code=409, detail="Вы уже авторизованы")
    user = await db.users.get_user_with_hashed_password(email=data.email)
    if not user:
        raise EmailNotRegisteredHTTPException
    if not AuthService().verify_password(data.password, user.hashed_password):
        raise IncorrectPasswordHTTPException
    access_token = AuthService().create_access_token({"user_id": user.id, "role_id": user.role_id})
    response.set_cookie("access_token", access_token, httponly=True)

    await db.commit()

    return {"message": "Вы успешно авторизовались", "access_token": access_token}


@router.get("/logout", summary="Выход пользователя")
def logout_user(response: Response, request: Request):
    if not request.cookies.get("access_token"):
        raise HTTPException(status_code=409, detail="Вы не авторизованы")
    response.delete_cookie("access_token")

    return {"message": "Выход из системы"}


@router.get("/me", summary="Получение текущего пользователя")
async def get_current_user(user_id: UserIdDep, db: DBDep):
    user = await db.users.get_one_or_none(id=user_id)

    return {"user": user}
