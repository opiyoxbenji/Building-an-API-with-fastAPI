"""create post table

Revision ID: 395dc74c5365
Revises: 
Create Date: 2023-02-07 13:48:03.749121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '395dc74c5365'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
