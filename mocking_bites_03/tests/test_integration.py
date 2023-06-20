from lib.secret_diary import *
from lib.diary import *


def test_pass_in_diary_to_secret_diary_and_then_try_to_read_it():
    diary = Diary('Diary entry')
    secret_diary = SecretDiary(diary)
    assert secret_diary.read() == "Go away!"

def test_unlocked_diary_returns_diary_contents():
    diary = Diary('Diary entry')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Diary entry"

def test_relocked_diary_returns_message():
    diary = Diary('Diary entry')
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    assert secret_diary.read() == "Go away!"
