from src.models import BooksModel, FilesModel
from src.repositories.base import BaseRepository
from src.schemas.book import BookReadSchema, FileReadSchema


class BookRepository(BaseRepository):
    model = BooksModel
    schema = BookReadSchema


class FileRepository(BaseRepository):
    model = FilesModel
    schema = FileReadSchema


