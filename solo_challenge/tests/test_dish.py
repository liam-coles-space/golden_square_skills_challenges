from lib.dish import *

def test_construct_dish():
    dish = Dish('Food', 15)
    assert dish.name == 'Food'
    assert dish.price == 15

"""
When format is called 
returns string formatting name and price
"""
def test_format_converts_name_and_price_correctly():
    dish = Dish('Chocolate Cake', 15)
    assert dish.format() == 'Chocolate Cake : £15.00'


