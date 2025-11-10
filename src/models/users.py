from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String

from src.database import Base


class UsersModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"))

    role: Mapped["RolesModel"] = relationship("RolesModel", back_populates="users")
    author_book: Mapped[list["BooksModel"]] = relationship("BooksModel", back_populates="author")
    reviews: Mapped[list["ReviewsModel"]] = relationship("ReviewsModel", back_populates="user")
    favorites: Mapped[list["FavoritesModel"]] = relationship("FavoritesModel", back_populates="user")
