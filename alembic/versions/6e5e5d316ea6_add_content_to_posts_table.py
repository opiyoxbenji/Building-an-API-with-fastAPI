"""add content to posts table

Revision ID: 6e5e5d316ea6
Revises: 395dc74c5365 
Create Date: 2023-02-07 13:58:01.656911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e5e5d316ea6'
down_revision = '395dc74c5365'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', content)
    pass
