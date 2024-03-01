"""Updating Foreign Key relationships

Revision ID: 1b8b8d9413ef
Revises: b678838d1256
Create Date: 2024-03-01 16:24:55.920924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b8b8d9413ef'
down_revision: Union[str, None] = 'b678838d1256'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        "fk_user_id",
        "links",
        "users",
        ["user_id"],
        ["id"],
    )


def downgrade():
    op.drop_constraint("fk_user_id", "links", type_="foreignkey")
