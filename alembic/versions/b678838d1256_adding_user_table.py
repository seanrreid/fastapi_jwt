"""Adding user table

Revision ID: b678838d1256
Revises: 21d5ebf12be5
Create Date: 2024-03-01 15:35:18.792499

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b678838d1256'
down_revision: Union[str, None] = '21d5ebf12be5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
