from lib.menu import *
from unittest.mock import Mock

def test_construct_menu():
    dish_mock1 = Mock()
    dish_mock2 = Mock()
    menu = Menu([dish_mock1, dish_mock2])
    assert menu.dish_list == [dish_mock1, dish_mock2]

"""
When list_dishes_with_price is called when dishes has multiple items
calls dish object method list_dishes and returns list from that method
"""
def test_list_dishes_with_prices_returns_list_with_names_and_prices():
    dish_mock1 = Mock()
    dish_mock2 = Mock()
    dish_mock1.format.return_value = 'Curry : £12.50'
    dish_mock2.format.return_value = 'Pizza : £8.50'
    menu = Menu([dish_mock1, dish_mock2])
    assert menu.list_dishes_with_price() == ['Curry : £12.50', 'Pizza : £8.50']
    assert dish_mock1.format.assert_called

"""
When find_dish is called when matching item is in dishes property
returns mathing dish object
"""
def test_find_dish_finds_correct_dish():
    dish_mock1 = Mock()
    dish_mock2 = Mock()
    dish_mock3 = Mock()
    dish_mock1.name = 'Pizza'
    dish_mock1.price = 8.50
    dish_mock2.name = 'Curry'
    dish_mock2.price = 4
    dish_mock3.name = 'Stew'
    dish_mock3.price = 12.30
    menu = Menu([dish_mock1, dish_mock2, dish_mock3])
    assert menu.find_dish('Stew') == dish_mock3

"""
When find_dish is called when matching item is not in dishes property
returns None
"""


