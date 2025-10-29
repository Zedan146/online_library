import typing

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database import Base


class GenresModel(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)

    books: Mapped[list["BooksModel"]] = relationship(
        "BooksModel", secondary="book_genres", back_populates="genres"
    )


class BookGenresModel(Base):
    __tablename__ = "book_genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id", ondelete="CASCADE"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genres.id", ondelete="CASCADE"))
