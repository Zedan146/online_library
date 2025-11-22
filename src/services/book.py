import os
import shutil

from fastapi import UploadFile

from src.models.books import FileType
from src.schemas.book import BookCreateSchema, FileCreateSchema
from src.services.base import BaseService


class BookService(BaseService):

    async def add_book(
            self,
            data: BookCreateSchema,
            cover_file_data: UploadFile,
            book_file_data: UploadFile,
    ):
        book = await self.db.books.add(data)

        if cover_file_data:
            _cover_data = self._save_file(cover_file_data, FileType.COVER, book_id=book.id)
            await self.db.files.add(_cover_data)

        if book_file_data:
            _book_data = self._save_file(book_file_data, FileType.BOOK, book_id=book.id)
            await self.db.files.add(_book_data)

        await self.db.commit()

        return await self.db.books.get_one_or_none(id=book.id)

    @staticmethod
    def _save_file(file: UploadFile, ftype: FileType, book_id: int) -> FileCreateSchema:
        upload_dir = f"src/upload/{ftype.value}"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = f"{upload_dir}/{file.filename}"
        with open(file_path, "wb") as new_file:
            shutil.copyfileobj(file.file, new_file)

        file_size = os.path.getsize(file_path)

        return FileCreateSchema(
            filename=file.filename,
            file_path=file_path,
            file_size=file_size,
            file_type=ftype,
            book_id=book_id
        )
