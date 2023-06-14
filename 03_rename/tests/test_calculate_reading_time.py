from lib.calculate_reading_time import *

def test_empty_string_returns_zero():
    assert calculate_reading_time("") == 0.0

def test_twenty_word_string_returns_correct_value():
    assert calculate_reading_time("One Two Three Four Five Six seven eight nine ten eleven twelve thirteen fourteen fitenfee sixteen seventeen eighteen nineteen twenty") == 0.1

def test_450_word_string_returns_correct_value():
    text = ""
    for i in range(450):
        text += 'word '
    
    assert calculate_reading_time(text) == 2.3
    
