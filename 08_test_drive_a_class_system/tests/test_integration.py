from lib.diary import *
from lib.diary_entry import *

#When we add two dirary entries
#We get the diary entries back in the entries list

def test_adds_multiple_diary_entries_and_lists_them():
    diary = Diary()
    entry1 = DiaryEntry('Number 1', 'Contents 1')
    entry2 = DiaryEntry('Number 2', 'Contents 2')
    entry3 = DiaryEntry('Number 3', 'Contents 3')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.all() == [entry1, entry2, entry3]

def test_count_words_returns_total_word_count_of_all_contents_in_diary_entries():
    diary = Diary()
    entry1 = DiaryEntry('Number 1', 'Contents Three Words')
    entry2 = DiaryEntry('Number 2', 'Contents Four Words Words')
    entry3 = DiaryEntry('Number 3', 'Contents Five Words Five Words')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.count_words() == 12

def test_add_multiple_diary_entries_and_returns_total_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Number 2', 'Contents Four Words Words')
    entry2 = DiaryEntry('Number 3', 'Contents Five Words Five Words')
    entry3 = DiaryEntry('Number 4', 'Contents Six Words Six Words Words')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.reading_time(3) == 5

def test_add_multiple_diary_entries_and_returns_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Number 2', 'Contents Four Words Words')
    entry2 = DiaryEntry('Number 3', 'Contents Five Words Five Words')
    entry3 = DiaryEntry('Number 4', 'Contents Six Words Six Words Words')
    diary.add(entry1)
    diary.add(entry2) 
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(3,2).title == entry3.title
    assert diary.find_best_entry_for_reading_time(3,2).contents == entry3.contents

def test_add_mutiple_diary_entries_higher_than_max_words_that_can_be_read():
    diary = Diary()
    entry1 = DiaryEntry('Number 2', 'Contents Four Words Words')
    entry2 = DiaryEntry('Number 3', 'Contents Five Words Five Words')
    entry3 = DiaryEntry('Number 4', 'Contents Six Words Six Words Words')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(1,3) == None



