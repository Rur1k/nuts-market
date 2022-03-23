"""empty message

Revision ID: 836c528e24fc
Revises: 4b479f31b45c
Create Date: 2022-03-23 10:56:57.585726

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from project import models


# revision identifiers, used by Alembic.
revision = '836c528e24fc'
down_revision = '4b479f31b45c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'date')
    # ### end Alembic commands ###

