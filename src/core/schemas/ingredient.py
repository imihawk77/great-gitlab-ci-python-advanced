from pydantic import BaseModel,  ConfigDict


class IngredientBase(BaseModel):
    ingredient_name: str = "Свинина"
    ingredient_description: str = "4 куска. 200 гр."


class IngredientCreate(IngredientBase):
    pass


class IngredientRead(IngredientBase):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id:int