from models.ingredient import Ingredient


def ingredient():
    ingredient = Ingredient('presunto')
    print('\n', '-------------------------------')
    print('ingredient.name ---> ', ingredient.name)
    print('ingredient.restrictions ---> ', ingredient.restrictions)
    print('\n', '-------------------------------')


ingredient()
