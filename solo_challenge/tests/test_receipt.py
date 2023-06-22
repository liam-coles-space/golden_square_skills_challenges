from lib.receipt import *

"""
When create is called with dictionary of 1 key value pair
returns formmated itemized list of 2 with total at the end
"""
def test_create_returns_single_item_receipt_as_list():
    receipt = Receipt()
    items = [{'Pizza': 14.80}]
    assert receipt.create(items) == ['Pizza £14.80', 'Total : £14.80']

"""
When create is called with list 4 dictionarys of name and price
returns formmated itemized list of 5 with total at the end
"""
def test_create_returns_multiple_item_receipt_as_list():
    receipt = Receipt()
    items = [{'Pizza': 14.80},{'Curry': 12.00},{'Cake': 3.00},{'Stew': 2.00}]
    assert receipt.create(items) == ['Pizza £14.80','Curry £12.00', 'Cake £3.00', 'Stew £2.00', 'Total : £31.80']

"""
When create is called with dictionary of list of 6 dictionaries (three duplicates)
returns formmated itemized list of 5 with total at the end
"""
def test_create_returns_multiple_items_with_duplicates_as_list():
    receipt = Receipt()
    items = [{'Pizza': 14.80}, {'Curry': 12.00}, {'Cake': 3.00}, {'Stew': 2.00}, {'Pizza': 14.80}, {'Pizza':14.80}]
    assert receipt.create(items) == ['Pizza £14.80','Curry £12.00', 'Cake £3.00', 'Stew £2.00', 'Pizza £14.80', 'Pizza £14.80', 'Total : £61.40']

"""
When create is called with dictionary of list of 0 dictionaries
returns empty list
"""
def test_create_returns_multiple_items_with_duplicates_as_list():
    receipt = Receipt()
    items = []
    assert receipt.create(items) == []
    
    
    

