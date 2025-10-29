"""fix relationships between models

Revision ID: a5df860be1a1
Revises: 63c16a583865
Create Date: 2025-10-29 17:05:53.492267

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a5df860be1a1"
down_revision: Union[str, Sequence[str], None] = "63c16a583865"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
