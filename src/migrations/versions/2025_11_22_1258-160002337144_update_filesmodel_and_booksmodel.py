"""update FilesModel and BooksModel

Revision ID: 160002337144
Revises: e785cd34d5aa
Create Date: 2025-11-22 12:58:39.403641

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "160002337144"
down_revision: Union[str, Sequence[str], None] = "e785cd34d5aa"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "files",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("filename", sa.String(length=255), nullable=False),
        sa.Column("file_path", sa.String(length=500), nullable=False),
        sa.Column("file_size", sa.Integer(), nullable=False),
        sa.Column(
            "file_type", sa.Enum("COVER", "BOOK", name="filetype"), nullable=False
        ),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("book_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["book_id"], ["books.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_files_id"), "files", ["id"], unique=False)
    op.drop_index(op.f("ix_books_and_cover_url_id"), table_name="books_and_cover_url")
    op.drop_table("books_and_cover_url")


def downgrade() -> None:
    op.create_table(
        "books_and_cover_url",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "filename", sa.VARCHAR(length=255), autoincrement=False, nullable=False
        ),
        sa.Column(
            "file_path", sa.VARCHAR(length=500), autoincrement=False, nullable=False
        ),
        sa.Column("file_size", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
        sa.Column(
            "cover_for_book_id", sa.INTEGER(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "book_file_for_book_id", sa.INTEGER(), autoincrement=False, nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["book_file_for_book_id"],
            ["books.id"],
            name=op.f("books_and_cover_url_book_file_for_book_id_fkey"),
        ),
        sa.ForeignKeyConstraint(
            ["cover_for_book_id"],
            ["books.id"],
            name=op.f("books_and_cover_url_cover_for_book_id_fkey"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("books_and_cover_url_pkey")),
    )
    op.create_index(
        op.f("ix_books_and_cover_url_id"), "books_and_cover_url", ["id"], unique=False
    )
    op.drop_index(op.f("ix_files_id"), table_name="files")
    op.drop_table("files")
