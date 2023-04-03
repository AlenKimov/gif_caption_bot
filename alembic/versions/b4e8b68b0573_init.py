"""init

Revision ID: b4e8b68b0573
Revises: 
Create Date: 2023-04-02 19:55:37.493789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4e8b68b0573'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('first_name', sa.String(length=120), nullable=True),
    sa.Column('last_name', sa.String(length=120), nullable=True),
    sa.Column('animation_file_id', sa.String(length=120), nullable=True),
    sa.Column('last_gif_created_at', sa.DateTime(), nullable=True),
    sa.Column('count_of_creations', sa.Integer(), nullable=False),
    sa.Column('font', sa.String(length=120), nullable=True),
    sa.Column('font_size', sa.SmallInteger(), nullable=False),
    sa.Column('font_color', sa.String(length=60), nullable=False),
    sa.Column('stroke', sa.Boolean(), nullable=False),
    sa.Column('stroke_color', sa.String(), nullable=False),
    sa.Column('position', sa.String(), nullable=False),
    sa.Column('transition', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('telegram_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###