from lib.diary_entry import *

def test_instance_variables_initalize_correctly():
    diary_entry = DiaryEntry("March", "This is the contents of a diary")
    assert diary_entry.title == "March"
    assert diary_entry.contents == "This is the contents of a diary"

def test_format_returns_string_with_title_and_contents():
    diary_entry = DiaryEntry("March", "This is the contents of a diary")
    assert diary_entry.format() == "March: This is the contents of a diary"

def test_count_words_returns_seven_when_contents_is_seven_words():
    diary_entry = DiaryEntry("March", "This is the contents of a diary")
    assert diary_entry.count_words() == 7

def test_reading_time_returns_correct_reading_time():
    diary_entry = DiaryEntry("March", "")
    assert diary_entry.reading_time(100) == 0
    assert diary_entry.reading_time(0) == 0
    diary_entry.contents = "one two three four five"
    assert diary_entry.reading_time(5) == 1
    assert diary_entry.reading_time(8) == 1

def test_reading_chunk_returns_blank_string_when_arguement_are_zero():
    diary_entry = DiaryEntry("March", "Text in here")
    assert diary_entry.reading_chunk(0,0) == ""

def test_first_reading_chunk_call_returns_correct_string():
    diary_entry = DiaryEntry("March", "Text in here now thanks")
    assert diary_entry.reading_chunk(2,2) == "Text in here now"

    
    
