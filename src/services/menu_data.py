# Req 3
from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        dish_prices = dict()

        df = pd.read_csv(source_path)

        price_data = df[['dish', 'price']].itertuples(index=False)

        for dish, price in price_data:
            dish_prices[dish] = price

        for dish in dish_prices.keys():
            dish_object = Dish(dish, dish_prices[dish])
            ingredient_data = df.loc[df['dish'] == dish].itertuples(
                index=False)
            for line_dish, price, ingredient, amount in ingredient_data:
                ingredient_object = Ingredient(ingredient)
                dish_object.add_ingredient_dependency(
                    ingredient_object, amount
                )
            self.dishes.add(dish_object)
