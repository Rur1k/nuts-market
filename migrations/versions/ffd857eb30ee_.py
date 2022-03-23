"""empty message

Revision ID: ffd857eb30ee
Revises: 4d63c2f9ad86
Create Date: 2022-03-23 16:03:53.905214

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from project import models


# revision identifiers, used by Alembic.
revision = 'ffd857eb30ee'
down_revision = '4d63c2f9ad86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('manager', sa.Integer(), nullable=True))
    op.drop_constraint('orders_manager_id_fkey', 'orders', type_='foreignkey')
    op.create_foreign_key(None, 'orders', 'user', ['manager'], ['id'])
    op.drop_column('orders', 'manager_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('manager_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.create_foreign_key('orders_manager_id_fkey', 'orders', 'user', ['manager_id'], ['id'])
    op.drop_column('orders', 'manager')
    # ### end Alembic commands ###

