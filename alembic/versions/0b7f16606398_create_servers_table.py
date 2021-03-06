"""create servers table

Revision ID: 0b7f16606398
Revises: 
Create Date: 2021-08-14 12:38:18.658304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b7f16606398'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('servers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.VARCHAR(length=512), nullable=True),
    sa.Column('alias', sa.VARCHAR(length=256), nullable=True),
    sa.Column('description', sa.VARCHAR(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias')
    )
    op.create_index(op.f('ix_servers_address'), 'servers', ['address'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_servers_address'), table_name='servers')
    op.drop_table('servers')
    # ### end Alembic commands ###
