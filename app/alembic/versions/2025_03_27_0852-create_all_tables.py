"""create_all_tables

Revision ID: ef80b5d86d71
Revises:
Create Date: 2025-03-27 08:52:39.557896

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "ef80b5d86d71"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "baskets",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id"),
    )
    op.create_table(
        "foods",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("photo", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_staff", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("telegram_id"),
    )
    op.create_table(
        "basket_food",
        sa.Column("basket_id", sa.Integer(), nullable=False),
        sa.Column("food_id", sa.Integer(), nullable=False),
        sa.Column("added_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["basket_id"],
            ["baskets.id"],
        ),
        sa.ForeignKeyConstraint(
            ["food_id"],
            ["foods.id"],
        ),
        sa.PrimaryKeyConstraint("basket_id", "food_id"),
    )
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("telegram_id", sa.String(), nullable=False),
        sa.Column("basket_id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.Column("customer_name", sa.String(length=255), nullable=False),
        sa.Column("customer_phone", sa.String(length=20), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "PENDING",
                "PROCESSING",
                "SHIPPED",
                "DELIVERED",
                "CANCELLED",
                "RETURNED",
                "FAILED",
                "ON_HOLD",
                name="order_status",
            ),
            nullable=False,
        ),
        sa.Column("total_price", sa.DECIMAL(precision=10, scale=2), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(
            ["basket_id"],
            ["baskets.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("orders")
    op.drop_table("basket_food")
    op.drop_table("users")
    op.drop_table("foods")
    op.drop_table("baskets")
