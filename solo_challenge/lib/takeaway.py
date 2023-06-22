from lib.order import *
from lib.menu import *

class TakeAway:
    # User facing properties:
    #   menu: list of instances of dish

    def __init__(self, menu, order):
        self.menu = menu
        self.order = order

    def get_menu_list(self):
        # returns:
        #   A list of of all the dish objects in the menu property formatted into strings in a list
        return self.menu.list_dishes_with_price()

    def add_to_order(self, dish_name, quantity):
        # parameters:
        #   dish_name: string value
        #   quantity: int
        # side effects:
        #   adds dish object to order_items list property in order object
        if self.order.add_order_item(dish_name, quantity) == False:
            return 'Error: Item does not exist'

    def remove_from_order(self, dish_name, quantity):
        # parameters:
        #   dish_name: string value
        #   quantity: int
        # side effects:
        #   removes dish object from order_items list property in order object
        return self.order.remove_order_item(dish_name, quantity)

    def complete_order(self, phone_number):
        # parameters:
        #   phone_number: string value
        # returns:
        #   itemized reciept in the form of a string
        # side-effects:
        #   calls comms object to send confirmation text
        
        self.order.send_confirmation_text(phone_number)
        receipt_list = self.order.generate_receipt()
        if receipt_list != []:
            return receipt_list
        else:
            return 'Cannot complete order. No items in basket'
            
