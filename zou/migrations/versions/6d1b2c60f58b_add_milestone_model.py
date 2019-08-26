"""Add milestone model

Revision ID: 6d1b2c60f58b
Revises: 10cf267d95c9
Create Date: 2019-08-22 23:34:32.450079

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import sqlalchemy_utils
import uuid

# revision identifiers, used by Alembic.
revision = '6d1b2c60f58b'
down_revision = '10cf267d95c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('milestone',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('project_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True),
    sa.Column('task_type_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), default=uuid.uuid4, nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['task_type_id'], ['task_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_milestone_project_id'), 'milestone', ['project_id'], unique=False)
    op.create_index(op.f('ix_milestone_task_type_id'), 'milestone', ['task_type_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_milestone_task_type_id'), table_name='milestone')
    op.drop_index(op.f('ix_milestone_project_id'), table_name='milestone')
    op.drop_table('milestone')
    # ### end Alembic commands ###