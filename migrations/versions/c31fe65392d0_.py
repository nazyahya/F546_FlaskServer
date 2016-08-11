"""empty message

Revision ID: c31fe65392d0
Revises: 9605afa9362b
Create Date: 2016-08-12 00:34:01.352481

"""

# revision identifiers, used by Alembic.
revision = 'c31fe65392d0'
down_revision = '9605afa9362b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('main_result', 'trace_max_ttl')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('main_result', sa.Column('trace_max_ttl', mysql.VARCHAR(length=50), nullable=True))
    ### end Alembic commands ###