from models.ingredient import Ingredient, Restriction
import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501


# Req 2
def test_dish():
    first_dish = Dish('alho e oleo', 24.50)
    second_dish = Dish('alho e oleo', 24.50)
    third_dish = Dish('carbonara', 29.50)
    ingredient = Ingredient('ovo')
    third_dish.add_ingredient_dependency(ingredient, 3)
    assert first_dish.name == 'alho e oleo'
    assert first_dish.__hash__() == second_dish.__hash__()
    assert first_dish.__hash__() != third_dish.__hash__()
    assert first_dish == second_dish
    assert first_dish != third_dish
    assert repr(first_dish) == "Dish('alho e oleo', R$24.50)"
    with pytest.raises(TypeError):
        assert Dish('bolonhesa', '')
    with pytest.raises(ValueError):
        assert Dish('bolonhesa', 0)
    assert third_dish.recipe.get(ingredient) == 3
    assert third_dish.get_restrictions() == {Restriction.ANIMAL_DERIVED}
    assert third_dish.get_ingredients() == {ingredient}
