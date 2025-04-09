"""создание таблиц

Revision ID: faea70d523c4
Revises:
Create Date: 2025-03-23 20:53:49.575819

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "faea70d523c4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ingredients",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("ingredient_name", sa.String(length=100), nullable=False),
        sa.Column("ingredient_description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ingredients")),
    )
    op.create_table(
        "recipes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("recipe_name", sa.String(length=100), nullable=False),
        sa.Column("cooking_time", sa.Integer(), nullable=False),
        sa.Column("views", sa.Integer(), nullable=False),
        sa.Column("recipe_description", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_recipes")),
    )
    op.create_table(
        "ingredients_in_recipes",
        sa.Column("recipe_id", sa.Integer(), nullable=False),
        sa.Column("ingredient_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.String(length=100), nullable=True),
        sa.ForeignKeyConstraint(
            ["ingredient_id"],
            ["ingredients.id"],
            name=op.f("fk_ingredients_in_recipes_ingredient_id_ingredients"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["recipe_id"],
            ["recipes.id"],
            name=op.f("fk_ingredients_in_recipes_recipe_id_recipes"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "recipe_id",
            "ingredient_id",
            name=op.f("pk_ingredients_in_recipes"),
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("ingredients_in_recipes")
    op.drop_table("recipes")
    op.drop_table("ingredients")
    # ### end Alembic commands ###
