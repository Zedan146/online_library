import typing
from datetime import datetime

from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database import Base


if typing.TYPE_CHECKING:
    from src.models.books import BooksModel
    from src.models.users import UsersModel


class FavoritesModel(Base):
    __tablename__ = "favorites"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    added_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user: Mapped["UsersModel"] = relationship("UsersModel", back_populates="favorites")
    book: Mapped["BooksModel"] = relationship("BooksModel", back_populates="favorites")