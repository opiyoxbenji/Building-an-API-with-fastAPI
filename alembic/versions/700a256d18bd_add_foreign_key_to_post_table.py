"""add foreign-key to post table

Revision ID: 700a256d18bd
Revises: 7ccb8a298f6a
Create Date: 2023-02-07 14:20:31.478340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '700a256d18bd'
down_revision = '7ccb8a298f6a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
