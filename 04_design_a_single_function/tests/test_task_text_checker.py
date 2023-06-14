from lib.task_text_checker import *

def test_empty_string_returns_false():
    assert task_text_checker("") == False

def test_text_containing_target_string_returns_false():
    assert task_text_checker("I am string with #TODO in it") == True

def test_text_not_containing_target_string_returns_false():
    assert task_text_checker("I am string") == False

def test_text_with_target_string_but_no_hash_returns_false():
    assert task_text_checker("I am string with TODO in it") == False

def test_text


