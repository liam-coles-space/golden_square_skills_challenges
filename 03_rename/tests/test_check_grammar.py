from lib.check_grammar import *

def test_empty_string_returns_false():
    assert check_grammar("") == False

def test_starts_upper_ends_full_stop():
    assert check_grammar("Text that ends with a full stop.") == True

def test_starts_upper_ends_exclamation_point():
    assert check_grammar("String that ends with a exclamation!") == True

def test_starts_upper_ends_question_mark():
    assert check_grammar("String that ends with a question?") == True

def test_starts_lower_ends_suitable_punctuation_mark():
    assert check_grammar("string that ends with a full stop.") == False
    assert check_grammar("text that ends with a exclamation point!") == False
    assert check_grammar("text that ends with a question mark?") == False

def test_starts_upper_ends_no_suitable_punctuation_on_end():
    assert check_grammar("text that has not punctuation on the end") == False
    assert check_grammar("string has comma on the end,") == False

def tests_starts_lower_ends_no_suitable_punctuation_on_end():
    assert check_grammar("text that no punctuation on the end") == False