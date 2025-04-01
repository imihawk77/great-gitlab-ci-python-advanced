from typing import List

from pydantic import BaseModel, ConfigDict


class RecipeBase(BaseModel):
    recipe_name: str = "Геза"
    cooking_time: int = 50
    views: int = 1
    recipe_description: str = "Нежные пельмени с хрустящей корочкой"


class IngredientsInRecipe(BaseModel):
    ingredient_id: int
    quantity: str = "Количество продуктов"


class RecipeCreate(RecipeBase):
    ingredients: List[IngredientsInRecipe]


class RecipeRead(RecipeBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int


class Ingredient(BaseModel):
    name: str
    description: str | None
    quantity: str | None


class RecipeDetail(BaseModel):
    id: int
    recipe_name: str
    cooking_time: int
    recipe_description: str
    views: int
    ingredients: List[Ingredient]
