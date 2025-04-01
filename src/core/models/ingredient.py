from typing import TYPE_CHECKING, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.models.base import Base
from src.core.models.mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from src.core.models.recipe import Recipe


class Ingredient(IntIdPkMixin, Base):
    """
    Класс описывающий ингредиенты

    """

    ingredient_name: Mapped[str] = mapped_column(String(100))
    ingredient_description: Mapped[str | None]

    used_in_recipe: Mapped[List["Recipe"]] = relationship(
        back_populates="used_ingredients", secondary="ingredients_in_recipes"
    )

    def __repr__(self):
        return (
            f"Ingredient(id={self.id}, ingredient_name={self.ingredient_name},"
            f"ingredient_description={self.ingredient_description})"
        )
