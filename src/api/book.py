from typing import Annotated, Optional

from fastapi import APIRouter, UploadFile, Form, File

from src.api.dep import DBDep, UserIdDep
from src.schemas.book import BookCreateSchema
from src.services.book import BookService

router = APIRouter(prefix="/books", tags=["Книги"])


@router.get("", summary="Получить все книги")
async def get_all_books(db: DBDep):
    return await db.books.get_all()


@router.post("", summary="Добавление книги")
async def create_book(
        title: Annotated[str, Form(title="Название книги")],
        description: Annotated[Optional[str], Form(title="Описание книги")],
        cover_file: Annotated[Optional[UploadFile], File(title="Обложка книги")],
        book_file: Annotated[Optional[UploadFile], File(title="Файл книги")],
        user_id: UserIdDep,
        db: DBDep,
):
    data = BookCreateSchema(title=title, description=description, author_id=user_id)

    return await BookService(db).add_book(
        data=data,
        cover_file_data=cover_file,
        book_file_data=book_file,
    )
