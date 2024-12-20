"""Add year column to Earthquake

Revision ID: 3978388f2c8b
Revises: 80f2a1e7a4a0
Create Date: 2024-11-28 11:22:23.660102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3978388f2c8b'
down_revision = '80f2a1e7a4a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('earthquakes', sa.Column('year', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('earthquakes', 'year')
    # ### end Alembic commands ###
