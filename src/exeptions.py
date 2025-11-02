from fastapi import HTTPException


class LibraryHTTPException(HTTPException):
    status_code = 500
    detail = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class EmailNotRegisteredHTTPException(LibraryHTTPException):
    status_code = 401
    detail = "Пользователь с таким email не зарегистрирован"


class UserEmailAlreadyExistsHTTPException(LibraryHTTPException):
    status_code = 409
    detail = "Пользователь с такой почтой уже существует"


class IncorrectPasswordHTTPException(LibraryHTTPException):
    status_code = 401
    detail = "Пароль неверный"


class NoAccessTokenHTTPException(LibraryHTTPException):
    status_code = 401
    detail = "Вы не предоставили токен доступа"


class ObjectAlreadyExistsHTTPException(LibraryHTTPException):
    status_code = 409
    detail = "Похожий объект уже существует"
