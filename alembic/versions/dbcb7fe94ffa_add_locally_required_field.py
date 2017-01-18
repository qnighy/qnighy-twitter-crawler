"""Add locally_required field.

Revision ID: dbcb7fe94ffa
Revises: 78aeb2aa8f6a
Create Date: 2017-01-18 13:54:49.650662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbcb7fe94ffa'
down_revision = '78aeb2aa8f6a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('media', sa.Column('locally_required', sa.Boolean(),
                                     nullable=True))
    op.create_index('ix_media_local_availability', 'media',
                    ['locally_required', 'locally_available'], unique=False)
    op.drop_index('ix_media_locally_available', table_name='media')


def downgrade():
    op.create_index('ix_media_locally_available', 'media',
                    ['locally_available'], unique=False)
    op.drop_index('ix_media_local_availability', table_name='media')
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_column('locally_required')
