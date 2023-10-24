"""empty message

Revision ID: b1687a18ebcb
Revises: b2b472dd16ac
Create Date: 2023-10-24 09:14:51.110079

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b1687a18ebcb'
down_revision = 'b2b472dd16ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('comment_text',
               existing_type=mysql.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.alter_column('comment_text',
               existing_type=mysql.TEXT(),
               nullable=False)

    # ### end Alembic commands ###
