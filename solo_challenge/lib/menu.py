from lib.dish import *

class Menu:
    # User facing properties:
    # None

    def __init__(self, dish_list):
        self.dish_list = dish_list

    def list_dishes_with_price(self):
        # returns:
        #   list of dish name and price as string value
        return [dish.format() for dish in self.dish_list]

    def find_dish(self, name):
        # Parameters:
        #   name : string value 
        # Returns : 
        #   dish object 
        for dish in self.dish_list:
            if dish.name == name:
                return dish