"""add relationship for book

Revision ID: dbea50f4ed0d
Revises: 160002337144
Create Date: 2025-11-22 20:56:12.218312

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "dbea50f4ed0d"
down_revision: Union[str, Sequence[str], None] = "160002337144"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
