"""Make locally_required nonnull.

Revision ID: b856dbe3d42b
Revises: dbcb7fe94ffa
Create Date: 2017-01-18 14:23:20.030220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b856dbe3d42b'
down_revision = 'dbcb7fe94ffa'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.alter_column('locally_required',
           existing_type=sa.BOOLEAN(),
           nullable=False)


def downgrade():
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.alter_column('locally_required',
            existing_type=sa.BOOLEAN(),
            nullable=True)
