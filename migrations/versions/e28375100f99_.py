"""empty message

Revision ID: e28375100f99
Revises: 5c651858b23e
Create Date: 2017-11-16 16:34:41.192665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e28375100f99'
down_revision = '5c651858b23e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('address', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('company', 'address')
    # ### end Alembic commands ###