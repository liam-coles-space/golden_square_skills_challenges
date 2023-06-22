from lib.order import *
from unittest.mock import Mock

def test_order_construct():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    assert order.delivery_time == 30    
    assert order.comms == comms_mock
    assert order.time == time_mock
    assert order.order_items == []
    assert order.menu == menu_mock
    assert order.receipt == receipt_mock

"""
when add_order_item is called with quantity of 1
correct dish object is added to order_items list
"""
def test_add_order_item_adds_retrieved_dish_to_order_items():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    dish_mock = Mock()
    receipt_mock = Mock()
    menu_mock.find_dish.return_value = dish_mock
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    order.add_order_item('Pizza', 1)
    assert order.order_items == [dish_mock]
    assert menu_mock.find_dish.assert_called

"""
when add_order_item is called with quantity of 3
correct dish object is added to order_items list 3 times
""" 
def test_add_order_item_quantity_3_adds_retrieved_dishes_to_order_items():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    dish_mock = Mock()
    receipt_mock = Mock()
    menu_mock.find_dish.return_value = dish_mock
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    order.add_order_item('Pizza', 3)
    assert order.order_items == [dish_mock, dish_mock, dish_mock]
    assert menu_mock.find_dish.assert_called

"""
when add_order_item is called with quantity of 3 but item is not present in menu objects dishes list
nothing is added to order_items list
""" 
def test_add_order_item_add_nothing_when_dish_not_found():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    menu_mock.find_dish.return_value = None
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    assert order.add_order_item('Pizza', 3) == False
    assert order.order_items == []
    assert menu_mock.find_dish.assert_called

"""
when remove_order_item is called with quantity of 1
matching dish object is removed from order_items list  
"""
def test_remove_order_item_removes_single_item_when_called_with_quantity_of_one():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    dish_mock1 = Mock()
    dish_mock1.name = 'Pizza'
    menu_mock.find_dish.return_value = dish_mock1
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    order.add_order_item('Pizza', 2)
    dish_mock2 = Mock()
    dish_mock2.name = 'Curry'
    menu_mock.find_dish.return_value = dish_mock2
    order.add_order_item('Curry', 1)
    order.remove_order_item('Pizza', 1)
    assert order.order_items == [dish_mock1, dish_mock2]
                                    

"""
when remove_order_item is called with quantity of 2
matching dish objects are removed from order_items list  
"""
def test_remove_order_item_removes_multiple_items_when_called_with_quantity_of_3():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    dish_mock1 = Mock()
    dish_mock1.name = 'Pizza'
    menu_mock.find_dish.return_value = dish_mock1
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    order.add_order_item('Pizza', 4)
    dish_mock2 = Mock()
    dish_mock2.name = 'Curry'
    menu_mock.find_dish.return_value = dish_mock2
    order.add_order_item('Curry', 3)
    order.remove_order_item('Pizza', 3)
    order.remove_order_item('Curry', 3)
    assert order.order_items == [dish_mock1]

"""
when remove_order_item is called with quantity of 2 but name of dish is not in order_items list
no objects are removed from item_list
"""
def test_remove_order_item_when_item_not_in_list():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    dish_mock1 = Mock()
    dish_mock1.name = 'Pizza'
    menu_mock.find_dish.return_value = dish_mock1
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    order.add_order_item('Pizza', 2)
    order.remove_order_item('Curry', 3)
    assert order.order_items == [dish_mock1, dish_mock1]


"""
when generate_receipt is called where items_list has one item 
The receipt object method create is called with a dictionary of one key value pair and generate_receipt returns receipt from create method
"""
def test_generate_receipt_for_one_item_returns_valid_list():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    receipt_mock.create.return_value = ['Pizza £10', 'Total £10']
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    dish_mock = Mock()
    dish_mock.name = 'Pizza'
    dish_mock.price = 10
    menu_mock.find_dish.return_value = dish_mock
    order.add_order_item('Pizza', 1)
    assert order.generate_receipt() == ['Pizza £10', 'Total £10']
    receipt_mock.create.assert_called_once_with([{'Pizza': 10}])

"""
when generate_receipt is called where items_list has no items 
returns None
"""
def test_generate_receipt_when_no_item_returns_empty_list():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    receipt_mock.create.return_value = []
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    assert order.generate_receipt() == []
"""
when generate_receipt is called where items_list has 3 items 
The receipt object method create is called with a dictionary of three key value pairs and generate_receipt returns list from create method
"""
def test_generate_receipt_for_three_items_returns_valid_list():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    receipt_mock.create.return_value = ['Pizza £10', 'Curry £15', 'Cake £5', 'Total £10']
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    dish_mock1 = Mock()
    dish_mock1.name = 'Pizza'
    dish_mock1.price = 10
    menu_mock.find_dish.return_value = dish_mock1
    order.add_order_item('Pizza', 1)
    dish_mock2 = Mock()
    dish_mock2.name = 'Curry'
    dish_mock2.price = 15
    menu_mock.find_dish.return_value = dish_mock2
    order.add_order_item('Curry', 1)
    dish_mock3 = Mock()
    dish_mock3.name = 'Cake'
    dish_mock3.price = 5
    menu_mock.find_dish.return_value = dish_mock3
    order.add_order_item('Cake', 1)
    assert order.generate_receipt() == ['Pizza £10', 'Curry £15', 'Cake £5', 'Total £10']
    receipt_mock.create.assert_called_once_with([{'Pizza': 10}, {'Curry': 15}, {'Cake': 5}])

"""
when send_confirmation_text is called with phone number
the comms object method send_text_message is called with phone_number and correctly formatted message, including correct delivery time
""" 
def test_send_confirmation_text_sets_up_message_correctly_and_calls_comms_object():
    comms_mock = Mock()
    time_mock = Mock()
    menu_mock = Mock()
    receipt_mock = Mock()
    time_mock.strftime.return_value = '11:51'
    time_mock.time.return_value = 1687431055
    time_mock.localtime.return_value = 100
    order = Order(30, comms_mock, time_mock, menu_mock, receipt_mock)
    order.send_confirmation_text('0178945521')
    comms_mock.send_text_message.assert_called_once_with('0178945521', 'Thank you! Your order was placed and will be delivered before 11:51')
