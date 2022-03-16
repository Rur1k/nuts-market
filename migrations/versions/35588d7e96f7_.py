"""empty message

Revision ID: 35588d7e96f7
Revises: 
Create Date: 2022-03-16 11:35:05.082656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35588d7e96f7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    # ### end Alembic commands ###
