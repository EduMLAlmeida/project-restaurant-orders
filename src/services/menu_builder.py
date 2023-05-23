import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        dishes_data = self.menu_data.dishes
        main_menu = list()
        for dish_data in dishes_data:
            dish_info = {
                'dish_name': dish_data.name,
                'price': dish_data.price,
                'ingredients': dish_data.get_ingredients(),
                'restrictions': dish_data.get_restrictions(),
            }
            if restriction not in dish_info['restrictions']:
                main_menu.append(dish_info)
        # print('\n', 'dishes_data ---> ', dishes_data, '\n')
        # print('\n', 'main_menu ---> ', main_menu, '\n')
        # print('\n', 'restriction ---> ', restriction, '\n')
        return pd.DataFrame(main_menu)
