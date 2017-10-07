"""empty message

Revision ID: 82e227787c88
Revises: c68573b23e0d
Create Date: 2017-10-08 03:28:56.842473

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '82e227787c88'
down_revision = 'c68573b23e0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=255), nullable=False))
    op.drop_column('user', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('name', mysql.VARCHAR(length=255), nullable=False))
    op.drop_column('user', 'username')
    # ### end Alembic commands ###