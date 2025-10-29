"""add ReviewsModel

Revision ID: 738aead75e72
Revises: a5df860be1a1
Create Date: 2025-10-29 17:12:04.096052

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "738aead75e72"
down_revision: Union[str, Sequence[str], None] = "a5df860be1a1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "reviews",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("comment", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("book_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["book_id"],
            ["books.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_reviews_id"), "reviews", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_reviews_id"), table_name="reviews")
    op.drop_table("reviews")
