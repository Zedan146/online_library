from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from src.models.books import FileType


class FileReadSchema(BaseModel):
    id: int
    filename: str
    file_size: int
    file_path: str
    file_type: FileType
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class FileCreateResponseSchema(BaseModel):
    filename: str
    file_size: int
    file_path: str
    file_type: FileType


class FileCreateSchema(FileCreateResponseSchema):
    book_id: Optional[int]


class BookCreateSchema(BaseModel):
    title: str
    description: Optional[str]
    author_id: int


class BookReadSchema(BookCreateSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    cover_image: Optional[FileReadSchema] = None
    book_file: Optional[FileReadSchema] = None

    model_config = ConfigDict(from_attributes=True)
