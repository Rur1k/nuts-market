"""empty message

Revision ID: b26843d8e978
Revises: 29563cac3883
Create Date: 2022-03-21 14:23:48.944475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b26843d8e978'
down_revision = '29563cac3883'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'vendor_code',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('product', 'composition',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('product', 'net_weight',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('product', 'energy_value',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'energy_value',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('product', 'net_weight',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('product', 'composition',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('product', 'vendor_code',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
