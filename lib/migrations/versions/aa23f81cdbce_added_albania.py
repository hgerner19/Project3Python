"""Added Albania

Revision ID: aa23f81cdbce
Revises: 5257b1d677dc
Create Date: 2023-04-18 17:55:28.216689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa23f81cdbce'
down_revision = '5257b1d677dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('libraries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('library_name', sa.String(), nullable=True),
    sa.Column('libray_address', sa.String(), nullable=True),
    sa.Column('library_city', sa.Integer(), nullable=True),
    sa.Column('library_state', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_name', sa.String(), nullable=True),
    sa.Column('owner_email', sa.String(), nullable=True),
    sa.Column('owner_phone', sa.Integer(), nullable=True),
    sa.Column('owner_address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('books_name', sa.String(), nullable=True),
    sa.Column('books_publisher', sa.String(), nullable=True),
    sa.Column('books_genre', sa.String(), nullable=True),
    sa.Column('books_pages', sa.Integer(), nullable=True),
    sa.Column('books_sales', sa.Integer(), nullable=True),
    sa.Column('books_price', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['owners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_table('owners')
    op.drop_table('libraries')
    # ### end Alembic commands ###