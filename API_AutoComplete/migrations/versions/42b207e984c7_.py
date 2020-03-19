"""empty message

Revision ID: 42b207e984c7
Revises: 
Create Date: 2020-03-13 14:47:54.373692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42b207e984c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('timeline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(), nullable=True),
    sa.Column('timestamp', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timeline')
    # ### end Alembic commands ###