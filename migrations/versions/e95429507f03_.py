"""empty message

Revision ID: e95429507f03
Revises: 82e227787c88
Create Date: 2017-10-08 04:00:04.899374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e95429507f03'
down_revision = '82e227787c88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('client_id', sa.String(length=100), nullable=False),
    sa.Column('client_secret', sa.String(length=50), nullable=False),
    sa.Column('_is_confidential', sa.Boolean(), nullable=False),
    sa.Column('_allowed_grant_types', sa.Text(), nullable=False),
    sa.Column('_redirect_uris', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_index(op.f('ix_client_client_secret'), 'client', ['client_secret'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_client_client_secret'), table_name='client')
    op.drop_table('client')
    # ### end Alembic commands ###
