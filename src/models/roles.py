import typing

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class RolesModel(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)

    users: Mapped[list["UsersModel"]] = relationship("UsersModel", back_populates='role')
