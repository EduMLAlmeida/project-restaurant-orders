from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    first_ingredient = Ingredient('presunto')
    second_ingredient = Ingredient('presunto')
    third_ingredient = Ingredient('salmão')
    ham_restrictions = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert first_ingredient.__hash__() == second_ingredient.__hash__()
    assert first_ingredient.__hash__() != third_ingredient.__hash__()
    assert first_ingredient == second_ingredient
    assert first_ingredient != third_ingredient
    assert repr(first_ingredient) == "Ingredient('presunto')"
    assert first_ingredient.name == 'presunto'
    assert first_ingredient.restrictions == ham_restrictions
