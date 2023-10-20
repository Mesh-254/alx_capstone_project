"""updated user model

Revision ID: 5bdda62446e4
Revises: 14095449cc4f
Create Date: 2023-10-19 18:21:39.119217

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5bdda62446e4'
down_revision = '14095449cc4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.VARCHAR(length=300),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=300),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###