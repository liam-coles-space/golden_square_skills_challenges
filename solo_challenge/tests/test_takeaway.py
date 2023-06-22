from lib.takeaway import *
from unittest.mock import Mock

def test_construct_takeaway():
    menu_mock = Mock()
    order_mock = Mock()
    takeaway = TakeAway(menu_mock, order_mock)
    assert takeaway.menu == menu_mock
    assert takeaway.order == order_mock

"""
When get_menu_list is called 
I get a list of strings containing a dish name and price formatted as Name:Price
"""
def test_get_menu_list_returns_correct_list():
    menu_mock = Mock()
    order_mock = Mock()
    menu_mock.list_dishes_with_price.return_value = ['Curry : £12.00', 'Pizza : £12.00']
    takeaway = TakeAway(menu_mock, order_mock)
    assert takeaway.get_menu_list() == ['Curry : £12.00', 'Pizza : £12.00']

"""
When add_to_order is called with quantity of 1
The order object method add_order_item is called
"""    
def test_add_order_item_calls_order_method_correctly():
    menu_mock = Mock()
    order_mock = Mock()
    takeaway = TakeAway(menu_mock, order_mock)
    takeaway.add_to_order('Curry', 1)
    order_mock.add_order_item.assert_called_once_with('Curry', 1)

"""
when add_to_order is called with quantity of 3
The order object method add_order_Item is called 
"""
def test_add_order_item_calls_order_method_correctly():
    menu_mock = Mock()
    order_mock = Mock()
    takeaway = TakeAway(menu_mock, order_mock)
    takeaway.add_to_order('Curry', 3)
    order_mock.add_order_item.assert_called_once_with('Curry', 3)

"""
when add order is called when order object method add_order_Item returns error message
Message of 'Error: Item does not exist' returned
"""
def test_add_order_item_calls_order_method_correctly():
    menu_mock = Mock()
    order_mock = Mock()
    order_mock.add_order_item.return_value = False
    takeaway = TakeAway(menu_mock, order_mock)
    assert takeaway.add_to_order('Curry', 3) == 'Error: Item does not exist'
    

"""
when remove_from_order is called with quantity of 1
The order object method remove_order_item is called
"""
def test_remove_order_item_calls_order_method_correctly():
    menu_mock = Mock()
    order_mock = Mock()
    takeaway = TakeAway(menu_mock, order_mock)
    takeaway.remove_from_order('Curry', 1)
    order_mock.remove_order_item.assert_called_once_with('Curry', 1)

"""
when remove_from_order is called with quantity of 4
The order object method remove_order_item is called
"""
def test_remove_order_item_for_quantity_of_three_calls_order_method_correctly():
    menu_mock = Mock()
    order_mock = Mock()
    takeaway = TakeAway(menu_mock, order_mock)
    takeaway.remove_from_order('Curry', 3)
    order_mock.remove_order_item.assert_called_once_with('Curry', 3)


"""
when complete_order is called with phone_number and items_list in order object has objects
The order object method generate_receipt is called and returns an itemized list. 
The order object send_confirmation_text is called with phone_number
"""
def test_complete_order_returns_receipt_and_passes_phone_number_to_order_object():
    menu_mock = Mock()
    order_mock = Mock()
    order_mock.generate_receipt.return_value = ['Pizza £8', 'Total £8']
    takeaway = TakeAway(menu_mock, order_mock)
    assert takeaway.complete_order('078945212') == ['Pizza £8', 'Total £8']
    order_mock.send_confirmation_text.assert_called_once_with('078945212')

"""
when complete_order is called with phone_number and items_list in order object has no objects
returns 'No items ordered'
"""
def test_complete_order_returns_message_when_no_items_ordered():
    menu_mock = Mock()
    order_mock = Mock()
    order_mock.generate_receipt.return_value = []
    takeaway = TakeAway(menu_mock, order_mock)
    assert takeaway.complete_order('078945212') == 'Cannot complete order. No items in basket'

