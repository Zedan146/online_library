from typing import Annotated

from fastapi import Depends, HTTPException, Request

from src.services.auth import AuthService


def get_token(request: Request) -> str:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Вы не предоставили токен доступа")
    return token


def get_current_user_id(token: str = Depends(get_token)) -> int:
    return AuthService().decode_token(token).get("user_id")


UserIdDep = Annotated[int, Depends(get_current_user_id)]
