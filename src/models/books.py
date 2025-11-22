import enum
import typing

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, String, Enum

from src.database import Base

if typing.TYPE_CHECKING:
    from src.models import *


class BooksModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    author: Mapped["UsersModel"] = relationship("UsersModel", back_populates="author_book")
    genres: Mapped[list["GenresModel"]] = relationship(
        "GenresModel", back_populates="books", secondary="book_genres"
    )
    reviews: Mapped[list["ReviewsModel"]] = relationship("ReviewsModel", back_populates="book")
    favorites: Mapped[list["FavoritesModel"]] = relationship("FavoritesModel", back_populates="book")
    files: Mapped[list["FilesModel"]] = relationship("FilesModel", back_populates="book")

    cover_image: Mapped[typing.Optional["FilesModel"]] = relationship(
        "FilesModel",
        primaryjoin="and_(BooksModel.id==FilesModel.book_id, FilesModel.file_type=='COVER')",
        uselist=False,
        viewonly=True
    )

    book_file: Mapped[typing.Optional["FilesModel"]] = relationship(
        "FilesModel",
        primaryjoin="and_(BooksModel.id==FilesModel.book_id, FilesModel.file_type=='BOOK')",
        uselist=False,
        viewonly=True
    )


class FileType(enum.Enum):
    COVER = "cover"
    BOOK = "book"


class FilesModel(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    filename: Mapped[str] = mapped_column(String(255))
    file_path: Mapped[str] = mapped_column(String(500))
    file_size: Mapped[int]
    file_type: Mapped[FileType] = mapped_column(Enum(FileType))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    book_id: Mapped[int | None] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"))

    book = relationship("BooksModel", back_populates="files")
