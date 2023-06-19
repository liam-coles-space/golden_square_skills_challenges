from lib.diary_entry import *

def test_construct_diary_entry():
    diary_entry = DiaryEntry('21-04-2013', "Diary entry 3",[],[])
    assert diary_entry.date == '21-04-2013'
    assert diary_entry.text == "Diary entry 3"
    assert diary_entry.todos == []
    assert diary_entry.phone_numbers == []

def test_count_words_returns_text_word_count():
    diary_entry = DiaryEntry('21-04-2013', "Diary entry 3",[],[])
    assert diary_entry.word_count() == 3

    