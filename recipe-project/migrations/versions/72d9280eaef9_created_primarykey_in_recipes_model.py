"""created primarykey in recipes model

Revision ID: 72d9280eaef9
Revises: b1687a18ebcb
Create Date: 2023-10-24 15:24:15.437233

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '72d9280eaef9'
down_revision = 'b1687a18ebcb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_index('spoonacular_id')
        batch_op.drop_column('spoonacular_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('spoonacular_id', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_index('spoonacular_id', ['spoonacular_id'], unique=False)

    # ### end Alembic commands ###