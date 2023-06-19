from lib.diary import *

def test_diary_construct():
    diary = Diary()
    assert diary._diary_entries == []

def test_all_returns_empty_list_when_no_diary_entries():
    diary = Diary()
    assert diary.all_diary_entries() == []

def test_get_diary_entry_for_reading_speed_and_time_returns_none_when_no_diary_entries():
    diary = Diary()
    assert diary.get_diary_entry_for_reading_speed_and_time(8,5) == None

def test_get_all_phone_numbers_returns_empty_list_when_no_diary_entries():
    diary = Diary()
    assert diary.get_all_phone_numbers() == []