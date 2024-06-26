"""empty message

Revision ID: f4d270825493
Revises: 
Create Date: 2022-04-02 23:12:34.583238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4d270825493'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('phone_no', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('Transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('trans_name', sa.String(length=50), nullable=False),
    sa.Column('trans_time', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Bill payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bill_payment_type', sa.String(length=50), nullable=False),
    sa.Column('bill_payment_amount', sa.Float(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['transaction_id'], ['Transactions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Card Transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('added_card', sa.Boolean(), nullable=False),
    sa.Column('added_card_time', sa.DateTime(), nullable=False),
    sa.Column('card_deposit_amount', sa.Float(), nullable=True),
    sa.Column('card_withdrawal_amount', sa.Float(), nullable=True),
    sa.Column('card_transaction_time', sa.DateTime(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['transaction_id'], ['Transactions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('In App transfers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ammount_sent', sa.Float(), nullable=True),
    sa.Column('ammount_received', sa.Float(), nullable=True),
    sa.Column('in_app_transfer_time', sa.DateTime(), nullable=False),
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['transaction_id'], ['Transactions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Loan Payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('loan_collected', sa.Float(), nullable=True),
    sa.Column('date_of_loan_collected', sa.DateTime(), nullable=True),
    sa.Column('loan_repaid', sa.Float(), nullable=True),
    sa.Column('date_of_loan_repaid', sa.DateTime(), nullable=True),
    sa.Column('transaction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['transaction_id'], ['Transactions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Loan Payments')
    op.drop_table('In App transfers')
    op.drop_table('Card Transactions')
    op.drop_table('Bill payments')
    op.drop_table('Transactions')
    op.drop_table('Users')
    # ### end Alembic commands ###
