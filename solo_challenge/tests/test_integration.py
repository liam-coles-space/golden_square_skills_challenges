from lib.takeaway import *
from lib.menu import *
from lib.dish import *
from lib.order import *
from lib.comms import *
from lib.receipt import *
from unittest.mock import Mock
from time import *
from twilio.rest import Client
import time_machine


"""
When I retrieve the menu list 
I get a list of strings, each of which contains a dish name and price
"""
def test_retrieve_menu_list():
    comms = Comms(Mock())
    receipt = Receipt()
    menu = Menu([Dish('Pizza', 14.80), Dish('Curry', 12.25), Dish('Chips', 6), Dish('Lasagne', 8.50), Dish('Beef Noodles', 11), Dish('Chocolate Cake', 6.50)])
    order = Order(30, comms, menu, receipt)
    takeaway = TakeAway(menu, order)
    assert takeaway.get_menu_list() == ['Pizza : £14.80', 'Curry : £12.25', 'Chips : £6.00', 'Lasagne : £8.50', 'Beef Noodles : £11.00', 'Chocolate Cake : £6.50']
    
    
"""
When I add a single item to my order and then complete my order
I get a itemised receipt in the form of a list of strings, including total, item name, item price and item quantity. Also a text message is sent to my phone number with a confirmation message
"""
def test_add_single_item_and_complete_order():
    traveler = time_machine.travel(1687431055, tick = False)
    traveler.start()
    twilio_mock = Mock()
    client_mock = Mock()
    messages_mock = Mock()
    twilio_mock.return_value = client_mock
    client_mock.messages = messages_mock
    comms = Comms(twilio_mock)
    receipt = Receipt()
    menu = Menu([Dish('Pizza', 14.80), Dish('Curry', 12.25), Dish('Chips', 6), Dish('Lasagne', 8.50), Dish('Beef Noodles', 11), Dish('Chocolate Cake', 6.50)])
    order = Order(30, comms, menu, receipt)
    takeaway = TakeAway(menu, order)
    takeaway.add_to_order('Pizza', 1)
    assert takeaway.complete_order('01773503406') == ['Pizza £14.80', 'Total : £14.80']
    messages_mock.create.assert_called_with(to='+441773503406', from_='++447897026700', body='Thank you! Your order was placed and will be delivered before 12:20')
    traveler.stop()
    
"""
When I add multiple items to my order and then complete my order
I get a itemised receipt in the form of a list of strings, including total, item name, item price and item quantity. Also a text message is sent to my phone number with a confirmation message
"""
def test_add_multilple_items_and_complete_order():
    traveler = time_machine.travel(1687431055, tick = False)
    traveler.start()
    twilio_mock = Mock()
    client_mock = Mock()
    messages_mock = Mock()
    twilio_mock.return_value = client_mock
    client_mock.messages = messages_mock
    comms = Comms(twilio_mock)
    receipt = Receipt()
    menu = Menu([Dish('Pizza', 14.80), Dish('Curry', 12.25), Dish('Chips', 6), Dish('Lasagne', 8.50), Dish('Beef Noodles', 11), Dish('Chocolate Cake', 6.50)])
    order = Order(30, comms, menu, receipt)
    takeaway = TakeAway(menu, order)
    takeaway.add_to_order('Pizza', 1)
    takeaway.add_to_order('Curry', 1)
    takeaway.add_to_order('Beef Noodles', 1)
    assert takeaway.complete_order('01773503401') == ['Pizza £14.80','Curry £12.25', 'Beef Noodles £11.00', 'Total : £38.05']
    messages_mock.create.assert_called_with(to='+441773503401', from_='++447897026700', body='Thank you! Your order was placed and will be delivered before 12:20')
    traveler.stop()
"""
When I add multiple items to my order, some of which have a quantity of more than one, and then complete my order
I get a itemised receipt in the form of a list of strings, including total, item name, item price and item quantity. Also a text message is sent to my phone number with a confirmation message
"""
def test_add_multilple_duplicate_items_and_complete_order():
    traveler = time_machine.travel(1687431055, tick = False)
    traveler.start()
    twilio_mock = Mock()
    client_mock = Mock()
    messages_mock = Mock()
    twilio_mock.return_value = client_mock
    client_mock.messages = messages_mock
    comms = Comms(twilio_mock)
    receipt = Receipt()
    menu = Menu([Dish('Pizza', 14.80), Dish('Curry', 12.25), Dish('Chips', 6), Dish('Lasagne', 8.50), Dish('Beef Noodles', 11), Dish('Chocolate Cake', 6.50)])
    order = Order(30, comms, menu, receipt)
    takeaway = TakeAway(menu, order)
    takeaway.add_to_order('Pizza', 1)
    takeaway.add_to_order('Curry', 3)
    takeaway.add_to_order('Beef Noodles', 2)
    assert takeaway.complete_order('01773503401') == ['Pizza £14.80','Curry £12.25', 'Curry £12.25', 'Curry £12.25', 'Beef Noodles £11.00', 'Beef Noodles £11.00', 'Total : £73.55']
    messages_mock.create.assert_called_with(to='+441773503401', from_='++447897026700', body='Thank you! Your order was placed and will be delivered before 12:20')
    traveler.stop()

"""
When I add multiple items to my order, some of which have a quantity of more than one, and then remove some of the items and then complete my order
I get a itemised receipt in the form of a list of strings, including total, item name, item price and item quantity. Also a text message is sent to my phone number with a confirmation message
"""
def test_add_and_remove_multiple_duplicate_items_and_complete_order():
    traveler = time_machine.travel(1687431055, tick = False)
    traveler.start()
    twilio_mock = Mock()
    client_mock = Mock()
    messages_mock = Mock()
    twilio_mock.return_value = client_mock
    client_mock.messages = messages_mock
    comms = Comms(twilio_mock)
    receipt = Receipt()
    menu = Menu([Dish('Pizza', 14.80), Dish('Curry', 12.25), Dish('Chips', 6), Dish('Lasagne', 8.50), Dish('Beef Noodles', 11), Dish('Chocolate Cake', 6.50)])
    order = Order(30, comms, menu, receipt)
    takeaway = TakeAway(menu, order)
    takeaway.add_to_order('Pizza', 1)
    takeaway.add_to_order('Curry', 3)
    takeaway.remove_from_order('Curry', 2)
    takeaway.add_to_order('Beef Noodles', 2)
    takeaway.remove_from_order('Beef Noodles', 1)
    takeaway.remove_from_order('Pizza', 1)
    assert takeaway.complete_order('01773503401') == ['Curry £12.25', 'Beef Noodles £11.00', 'Total : £23.25']
    messages_mock.create.assert_called_with(to='+441773503401', from_='++447897026700', body='Thank you! Your order was placed and will be delivered before 12:20')
    traveler.stop()

"""
When I add multiple items to my order, some of which have a quantity of more than one, and then remove all of the items and then complete my order
No text message is sent and no receipt is generated
Error message is returned
"""
def test_add_and_remove_all_items_and_complete_order():
    traveler = time_machine.travel(1687431055, tick = False)
    traveler.start()
    twilio_mock = Mock()
    client_mock = Mock()
    messages_mock = Mock()
    twilio_mock.return_value = client_mock
    client_mock.messages = messages_mock
    comms = Comms(twilio_mock)
    receipt = Receipt()
    menu = Menu([Dish('Pizza', 14.80), Dish('Curry', 12.25), Dish('Chips', 6), Dish('Lasagne', 8.50), Dish('Beef Noodles', 11), Dish('Chocolate Cake', 6.50)])
    order = Order(30, comms, menu, receipt)
    takeaway = TakeAway(menu, order)
    assert takeaway.complete_order('01773503401') == 'Cannot complete order. No items in basket'
    traveler.stop()
