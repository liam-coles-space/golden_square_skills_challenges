from lib.diary_entry import *

def test_diary_entry_construction_gets_title_and_contents():
    diary_entry = DiaryEntry('Title 1', 'Contents 1')
    assert diary_entry.title == 'Title 1'
    assert diary_entry.contents == 'Contents 1'
    assert diary_entry.progress == 0

def test_count_words_gets_number_of_words_in_content():
    diary_entry = DiaryEntry('Title 1', 'Three whole words')
    assert diary_entry.count_words() == 3

def test_reading_time_gets_time_to_read_content():
    diary_entry = DiaryEntry('Title 1', 'Six whole words Six whole words')
    assert diary_entry.reading_time(2) == 3

def test_reading_chunk_gets_chunk_of_content_to_read():
    diary_entry = DiaryEntry('Title 1', 'Six whole words Six whole words')
    assert diary_entry.reading_chunk(2,2) == 'Six whole words Six'

def test_reading_chunk_second_call_gets_chunk_of_content_to_read():
    diary_entry = DiaryEntry('Title 1', 'Eight whole words Eight whole words Eight whole')
    diary_entry.reading_chunk(2,2)
    assert diary_entry.reading_chunk(3,1) == 'whole words Eight'

def test_reading_chunk_third_call_gets_chunk_of_content_to_read():
    diary_entry = DiaryEntry('Title 1', 'Eight goose words Eight snake words Eight whole')
    diary_entry.reading_chunk(2,2)
    diary_entry.reading_chunk(3,1)
    assert diary_entry.reading_chunk(1,2) == 'whole'

def test_counts_words_when_contents_is_blank():
    diary_entry = DiaryEntry('Title 1', '')
    assert diary_entry.count_words() == 0

def test_reading_time_when_contents_is_blank():
    diary_entry = DiaryEntry('Title 1', '')
    assert diary_entry.reading_time(7) == 0

def test_reading_chunk_when_contents_is_blank():
    diary_entry = DiaryEntry('Title 1', '')
    assert diary_entry.reading_chunk(7,4) == ''
    assert diary_entry.reading_chunk(7,4) == ''





