from lib.diary import *

def test_construct_diary():
    diary = Diary('Diary entry 1')
    assert diary.contents == 'Diary entry 1'

def test_read_returns_diary_contents():
    diary = Diary('Diary entry 1')
    assert diary.read() == 'Diary entry 1'   

