from typing import Optional, List
from beanie import Document
from pydantic import BaseModel, Field


class IngredientQuantity(BaseModel):
    quantity: Optional[float]
    unit: Optional[str]


class Ingredient(BaseModel):
    name: str
    quantity: Optional["IngredientQuantity"]


class Cocktail(Document):
    class Settings:
        name = "recipes"

    name: str
    ingredients: List["Ingredient"]
    instructions: List[str]


class IngredientAggregation(BaseModel):
    """A model for an ingredient count."""

    id: str = Field(None, alias="_id")
    total: int


Cocktail.model_rebuild()
Ingredient.model_rebuild()
