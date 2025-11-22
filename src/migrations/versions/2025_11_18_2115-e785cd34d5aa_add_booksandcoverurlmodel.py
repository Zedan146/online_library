"""add BooksAndCoverUrlModel

Revision ID: e785cd34d5aa
Revises: 738aead75e72
Create Date: 2025-11-18 21:15:51.489591

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = "e785cd34d5aa"
down_revision: Union[str, Sequence[str], None] = "738aead75e72"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "books_and_cover_url",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("filename", sa.String(length=255), nullable=False),
        sa.Column("file_path", sa.String(length=500), nullable=False),
        sa.Column("file_size", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("cover_for_book_id", sa.Integer(), nullable=True),
        sa.Column("book_file_for_book_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["book_file_for_book_id"],
            ["books.id"],
        ),
        sa.ForeignKeyConstraint(
            ["cover_for_book_id"],
            ["books.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_books_and_cover_url_id"), "books_and_cover_url", ["id"], unique=False
    )
    op.add_column("books", sa.Column("updated_at", sa.DateTime(), nullable=False))
    op.drop_column("books", "cover_image_url")
    op.drop_column("books", "file_url")
    op.drop_column("books", "update_at")


def downgrade() -> None:
    op.add_column(
        "books",
        sa.Column(
            "update_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "books", sa.Column("file_url", sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "books",
        sa.Column("cover_image_url", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_column("books", "updated_at")
    op.drop_index(op.f("ix_books_and_cover_url_id"), table_name="books_and_cover_url")
    op.drop_table("books_and_cover_url")
