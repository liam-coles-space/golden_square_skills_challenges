from lib.phone_number import *

def test_construct_phone_number():
    phone_number = PhoneNumber('Gary', '245789')
    assert phone_number._name == 'Gary'
    assert phone_number._number == '245789'