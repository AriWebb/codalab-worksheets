"""Replace time quota with parallel run quota

Revision ID: 59b16cf1146d
Revises: e3ec3926c0fc
Create Date: 2019-06-03 20:28:23.601957

"""

# revision identifiers, used by Alembic.
revision = '59b16cf1146d'
down_revision = '53bcf87ddf40'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('parallel_run_quota', sa.Integer(), nullable=False, server_default='3'))
    op.drop_column('user', 'time_quota')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('time_quota', mysql.FLOAT(), nullable=False))
    op.drop_column('user', 'parallel_run_quota')
    # ### end Alembic commands ###
