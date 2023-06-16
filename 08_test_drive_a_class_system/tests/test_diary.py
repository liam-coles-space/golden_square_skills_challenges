from lib.diary import *

def test_diary_construction_creates_empty_entry_list():
    diary = Diary()
    assert diary.entries_list == []

def test_count_words_when_no_diary_entry():
    diary = Diary()
    assert diary.count_words() == 0

def test_reading_time_when_no_diary_entry():
    diary = Diary()
    assert diary.reading_time(4) == 0

def test_all_when_no_diary_entry():
    diary = Diary()
    assert diary.all() == []

def test_find_best_entry_for_reading_time_when_no_diary_entry():
    diary = Diary()
    assert diary.find_best_entry_for_reading_time(4,8) == None




