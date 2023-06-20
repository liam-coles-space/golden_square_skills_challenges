from lib.secret_diary import *
from unittest.mock import Mock

def test_secret_diary_construct():
    diary_mock = Mock()
    secret_diary = SecretDiary(diary_mock)
    assert secret_diary.diary == diary_mock
    assert secret_diary.locked == True

def test_read_returns_message_straight_after_intialisation():
    diary_mock = Mock()
    secret_diary = SecretDiary(diary_mock)
    assert secret_diary.read() == 'Go away!'
    diary_mock.assert_not_called()

def test_unlock_changes_diary_to_unlocked():
    diary_mock = Mock()
    secret_diary = SecretDiary(diary_mock)
    secret_diary.unlock() 
    assert secret_diary.locked == False

def test_read_returns_unlocked_diary_contents():
    diary_mock = Mock()
    diary_mock.read.return_value = 'Diary entry 1'
    secret_diary = SecretDiary(diary_mock)
    secret_diary.unlock()
    assert secret_diary.read() == 'Diary entry 1' 

def test_lock_changes_diary_back_to_locked():
    diary_mock = Mock()
    secret_diary = SecretDiary(diary_mock)
    secret_diary.unlock() 
    secret_diary.lock()
    assert secret_diary.locked == True
    



