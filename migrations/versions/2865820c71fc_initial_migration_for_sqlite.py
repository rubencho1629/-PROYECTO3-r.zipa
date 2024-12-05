"""Initial migration for SQLite

Revision ID: 2865820c71fc
Revises: 
Create Date: 2024-12-05 18:15:59.933857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2865820c71fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('ingredientes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('es_sano', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('productos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('base_id', sa.Integer(), nullable=False),
    sa.Column('calorias', sa.Float(), nullable=True),
    sa.Column('rentabilidad', sa.Float(), nullable=True),
    sa.Column('costo_produccion', sa.Float(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('stock_maximo', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['base_id'], ['bases.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productos')
    op.drop_table('usuarios')
    op.drop_table('ingredientes')
    op.drop_table('bases')
    # ### end Alembic commands ###
