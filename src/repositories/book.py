from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models import BooksModel, FilesModel
from src.repositories.base import BaseRepository
from src.schemas.book import BookReadSchema, FileReadSchema


class BookRepository(BaseRepository):
    model = BooksModel
    schema = BookReadSchema

    async def get_one(self, **filter_by) -> BaseModel:
        query = (
            select(self.model).options(selectinload(self.model.files)).filter_by(**filter_by)
        )
        result = await self.session.execute(query)
        model = result.scalar_one()
        return self.schema.model_validate(model)

    async def get_all_with_files(self) -> list[BookReadSchema]:
        query = (
            select(self.model)
            .options(
                selectinload(BooksModel.cover_image),
                selectinload(BooksModel.book_file)
            )
        )
        result = await self.session.execute(query)
        books = result.scalars().all()
        return [BookReadSchema.model_validate(book) for book in books]


class FileRepository(BaseRepository):
    model = FilesModel
    schema = FileReadSchema


