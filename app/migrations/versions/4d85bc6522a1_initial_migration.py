"""Initial migration.

Revision ID: 4d85bc6522a1
Revises: 
Create Date: 2023-09-24 08:48:02.968566

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4d85bc6522a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.alter_column('fullname',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               type_=sa.String(length=80),
               nullable=False)
        batch_op.alter_column('phone',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               type_=sa.String(length=20),
               existing_nullable=True)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               type_=sa.String(length=120),
               nullable=True)
        batch_op.drop_index('email')

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               type_=sa.String(length=80),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               type_=sa.String(length=120),
               nullable=False)
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('email',
               existing_type=sa.String(length=120),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               nullable=True)
        batch_op.alter_column('password',
               existing_type=sa.String(length=120),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               existing_nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.String(length=80),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               existing_nullable=False)

    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=120),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=100),
               nullable=False)
        batch_op.alter_column('phone',
               existing_type=sa.String(length=20),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               existing_nullable=True)
        batch_op.alter_column('fullname',
               existing_type=sa.String(length=80),
               type_=mysql.VARCHAR(collation='utf8mb4_unicode_ci', length=255),
               nullable=True)

    # ### end Alembic commands ###
