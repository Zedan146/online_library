from datetime import datetime, timezone, timedelta

import jwt
from fastapi import HTTPException
from jwt.exceptions import DecodeError
from pwdlib import PasswordHash

from src.config import settings


class AuthService:
    password_hash = PasswordHash.recommended()

    def verify_password(self, plain_password, hashed_password) -> bool:
        return self.password_hash.verify(plain_password, hashed_password)

    def get_hashed_password(self, password: str) -> str:
        return self.password_hash.hash(password)

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_token(token: str) -> dict:
        try:
            return jwt.decode(token, key=settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
        except DecodeError:
            raise HTTPException(status_code=401, detail="Неверный токен доступа")
