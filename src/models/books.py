import typing

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, DateTime, String

from src.database import Base


if typing.TYPE_CHECKING:
    from src.models import reviews, favorites, users, genres


class BooksModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str | None]
    cover_image_url: Mapped[str | None]
    file_url: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    update_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    author: Mapped["users.UsersModel"] = relationship("UsersModel", back_populates="author_book")
    genres: Mapped[list["genres.GenresModel"]] = relationship(
        "GenresModel", back_populates="books", secondary="book_genres"
    )
    reviews: Mapped[list["reviews.ReviewsModel"]] = relationship("ReviewsModel", back_populates="book")
    favorites: Mapped[list["favorites.FavoritesModel"]] = relationship("FavoritesModel", back_populates="book")

