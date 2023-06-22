As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

#use python-twilipi to implement below
As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

class TakeAway:
    # User facing properties:
    #   None

    def __init__(self, menu):
        pass

    def get_menu_list(self):
        # returns:
        #   A list of of all the dish objects in the menu property formatted into strings in a list
        pass

    def add_to_order(self, dish_name, quantity)
        # parameters:
        #   dish_name: string value
        #   quantity: int
        # side effects:
        #   adds dish object to order_items list property in order object
        pass

    def remove_from_order(self, dish_name, quantity):
        # parameters:
        #   dish_name: string value
        #   quantity: int
        # side effects:
        #   removes dish object from order_items list property in order object
        pass

    def complete_order(self, phone_number)
        # parameters:
        #   phone_number: string value
        # returns:
        #   itemized reciept in the form of a string
        # side-effects:
        #   calls comms object to send confirmation text
        pass

class Order:
    # User facing properties:
    #   none

    def __init__(self, delivery_time):
        pass

    def add_order_item(self, name, quantity):
        # Parameters:
        #   name: string value
        #   quantity: int
        # Side-effects:
        #   adds dish object to order_items list property
        pass

    def remove_order_item(self, name, quantity):
        # Parameters:
        #   name: string value
        #   quantity: int
        # Side-effects:
        #   removes dish object from order_items list property
        pass

    def generate_receipt(self):
        # Parameters: 
        # Returns : string value showing an itemized bill with total
        pass

    def send_confirmation_text(self, phone_number)
        # Parameters:
        #   phone_number: string value
        #   time: int value 
        # Side effects:
            Calls comms.send_text_message which sends out text message 
        pass
    
class Receipt:
    # User facing properties:
    #   None

    def __init__(self):
        pass

    def create(self, items):
        # Parameters:
        #   items: dictionary of items(key) and prices(value)
        # Returns:
        #   list of itemised recipt with total
        pass

class Menu:
    # User facing properties:
    # None

    def __init__(self, dishes):
        pass

    def list_dishes_with_price():
        # returns:
        #   list of dish name and price as string value
        pass

    def find_dish(self, name):
        # Parameters:
        #   name : string value 
        # Returns : 
        #   dish object 
        pass

class Dish:
    # User facing properties:
    #   name : string value
    #   price: int value

    def __init__(self, name, price):
        pass

    def format(self):
        # returns:
        #   string value
        pass

class Comms:
    # User facing properties:
    #   None

    def __init__(self):
        pass

    def send_text_message(phone_number, message):
        # Parameters:
        #   phone_number: string value
        #   message: string value
        # Side effects: 
        #   sends text message

Integration Test cases:
""""
When I retrieve the menu list 
I get a list of strings, each of which contains a dish name and price
""""

""""
When I add multiple items to my order and then complete my order
I get a itemised receipt in the form of a list of strings, including total, item name, item price and item quantity. Also a text message is sent to my phone number with a confirmation message
""""

""""
When I add multiple items to my order, some of which have a quantity of more than one, and then complete my order
I get a itemised receipt in the form of a list of strings, including total, item name, item price and item quantity. Also a text message is sent to my phone number with a confirmation message
""""

""""
When I add multiple items to my order, some of which have a quantity of more than one, and then remove some of the items and then complete my order
I get a itemised receipt in the form of a list of strings, including total, item name, item price and item quantity. Also a text message is sent to my phone number with a confirmation message
""""

""""
When I add multiple items to my order, some of which have a quantity of more than one, and then remove all of the items and then complete my order
No text message is sent and no receipt is generated
""""

Unit tests:
Takeaway -

"""
When get_menu_list is called 
I get a list of strings containing a dish name and price formatted as Name:Price
"""

"""
When add_to_order is called with quantity of 1
The order object method add_order_item is called
"""

"""
when add_to_order is called with quantity of 3
The order object method add_order_Item is called 
"""

"""
when add order is called when item name does not exist in menu dishes property
Message of 'Error: Item does not exist' returned
"""

"""
when remove_from_order is called with quantity of 1
The order object method remove_order_item is called
"""

"""
when remove_from_order is called with quantity of 4
The order object method remove_order_item is called
"""

"""
when complete_order is called with phone_number and items_list in order object has objects
The order object method generate_receipt is called and returns an itemized list. 
The order object send_confirmation_text is called with phone_number
"""

"""
when complete_order is called with phone_number and items_list in order object has no objects
returns 'No items ordered'
"""

Order -
"""
when add_order_item is called with quantity of 1
correct dish object is added to order_items list
"""

"""
when add_order_item is called with quantity of 3
correct dish object is added to order_items list 3 times
""" 

"""
when add_order_item is called with quantity of 3 but item is not present in menu objects dishes list
nothing is added to order_items list
""" 

"""
when remove_order_item is called with quantity of 1
matching dish object is removed from order_items list  
"""

"""
when remove_order_item is called with quantity of 2
matching dish objects are removed from order_items list  
"""

"""
when remove_order_item is called with quantity of 2 but name of dish is not in order_items list
no objects are removed from item_list
"""

"""
when generate_receipt is called where items_list has one item 
The receipt object method create is called with a dictionary of one key value pair and generate_receipt returns receipt from create method
"""

"""
when generate_receipt is called where items_list has no items 
returns None
"""

"""
when generate_receipt is called where items_list has 3 items 
The receipt object method create is called with a dictionary of three key value pairs and generate_receipt returns list from create method
"""

"""
when send_confirmation_text is called with phone number
the comms object method send_text_message is called with phone_number and correctly formatted message, including correct delivery time
"""

Receipt -
"""
When create is called with dictionary of 1 key value pair
returns formmated itemized list of 2 with total at the end
"""

"""
When create is called with dictionary of 4 key value pair
returns formmated itemized list of 5 with total at the end
"""

"""
When create is called with dictionary of 6 key value pair (three duplicates)
returns formmated itemized list of 5 with total at the end
"""

Comms -

"""
When send_text_message is called with phone_number and message
twilio helper method create should be called with phone_number and message
"""

Menu - 

"""
When list_dishes_with_price is called when dishes has multiple items
calls dish object method list_dishes and returns list from that method
"""

"""
When find_dish is called when matching item is in dishes property
returns mathing dish object
"""

"""
When find_dish is called when matching item is not in dishes property
returns None
"""

Dish -
"""
When format is called 
returns string formatting name and price
"""
































