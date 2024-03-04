"""Adding Foreign Key constraint

Revision ID: 29719a32d65c
Revises: aceff0440eb9
Create Date: 2024-03-03 19:42:19.042535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29719a32d65c'
down_revision: Union[str, None] = 'aceff0440eb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'links', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'links', type_='foreignkey')
    # ### end Alembic commands ###