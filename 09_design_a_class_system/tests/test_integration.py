from lib.diary import *
from lib.phone_number import *
from lib.todo import *
from lib.diary_entry import *

def test_adds_multiple_diary_entries_and_lists_them():
    diary = Diary()
    phone_numbers = [PhoneNumber("Gary Man","0123456"), PhoneNumber("Mary Lamb","0789123")]
    todo_list = [Todo('Cleaning'), Todo("Shopping")]
    entry1 = DiaryEntry('03-04-2023', 'Diary entry 1', todo_list, phone_numbers)
    phone_numbers = [PhoneNumber("Adam Tiger","0654321"), PhoneNumber("Ann Horse","987654")]
    todo_list = [Todo('Running'), Todo("Driving")]
    entry2 = DiaryEntry('05-05-2023', 'Diary entry 2', todo_list, phone_numbers)
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all_diary_entries() == [entry1, entry2]

def test_diary_entry_reading_speed_and_time_returns_correct_entry():
    diary = Diary()
    phone_numbers = [PhoneNumber("Gary Man","0123456"), PhoneNumber("Mary Lamb","0789123")]
    todo_list = [Todo('Cleaning'), Todo("Shopping")]
    entry1 = DiaryEntry('03-04-2023', 'Diary entry length four', todo_list, phone_numbers)
    entry2 = DiaryEntry('05-05-2023', 'Diary entry length is five', todo_list, phone_numbers)
    entry3 = DiaryEntry('07-09-2023', 'Diary length three', todo_list, phone_numbers)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.get_diary_entry_for_reading_speed_and_time(3,2) == entry2

def test_get_all_phone_numbers_returns_all_phone_number_objects():
    diary = Diary()
    phone_number1 = PhoneNumber("Gary Man","0123456")
    phone_number2 = PhoneNumber("Mary Lamb","0789123")
    todo_list = [Todo('Cleaning'), Todo("Shopping")]
    entry1 = DiaryEntry('03-04-2023', 'Diary entry length four', todo_list, [phone_number1, phone_number2])
    phone_number3 = PhoneNumber("Gary Horse","01244456")
    phone_number4 = PhoneNumber("Barry Sheep","075678123")
    entry2 = DiaryEntry('05-05-2023', 'Diary entry length is five', todo_list, [phone_number3, phone_number4])
    diary.add(entry1)
    diary.add(entry2)
    assert diary.get_all_phone_numbers() == [phone_number1, phone_number2, phone_number3, phone_number4]

def test_find_diary_by_date_returns_diary_for_date():
    diary = Diary()
    phone_numbers = [PhoneNumber("Gary Man","0123456"), PhoneNumber("Mary Lamb","0789123")]
    todo_list = [Todo('Cleaning'), Todo("Shopping")]
    entry1 = DiaryEntry('03-04-2023', 'Diary entry length four', todo_list, phone_numbers)
    entry2 = DiaryEntry('05-05-2023', 'Diary entry length is five', todo_list, phone_numbers)
    entry3 = DiaryEntry('07-09-2023', 'Diary length three', todo_list, phone_numbers)
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    diary.find_diary_entry_by_date('05-05-2023')