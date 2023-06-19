from lib.diary_entry import *

class Diary:
    # User_facing properties:
    #    diary_entries: dictionary of instances of DiaryEntry

    def __init__(self):
        self._diary_entries = []

    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: instance of DiaryEntry
        # Side -effects:
        #   adds the diary_entry to the diary_entries property of the self object
        self._diary_entries.append(diary_entry)

    def all_diary_entries(self):
        # Returns:
        #   A list of all the diary_entry objects in the diary_entries propery
        return self._diary_entries
    
    def get_diary_entry_for_reading_speed_and_time(self, WPM, Minutes):
        # Parameters: 
        #   WPM: int
        #   Minutes: int
        # Returns:
        #   The diary entry object that has the text property that has the closest number of words (equal or less) to the WPM * Minutes
        diary_entry = ''
        current_count = 0
        for entry in self._diary_entries:
            if entry.word_count() <= WPM * Minutes and entry.word_count() > current_count:
                current_count = entry.word_count()
                diary_entry = entry
        if current_count > 0:
            return diary_entry


    def get_all_phone_numbers(self): 
        # Returns:
        #   A dictionary of all the PhoneNumber objects in each of the diary entry objects stored in the diary_entry property
        all_numbers = []
        for entry in self._diary_entries:
            all_numbers.extend(entry.phone_numbers)
        return all_numbers


    def find_diary_entry_by_date(self, date):
        # Parameters:
        #   Date: date value in format (dd-mm-yyyy) 
        # Returns:
        #   diary_entry object from diary_entries property that corresponds with 
        #   date arguement. If not found then None
        for entry in self._diary_entries:
            if entry.date == date:
                return entry

    def mark_task_as_complete(self, date, task):
        # Parameters:
        #   Date: date value in format (dd-mm-yyyy) 
        #   Task: string value
        # Side effect:
        #   Marks single task in single diary entry as complete
        diary_entry = self.find_diary_entry_by_date(date)
        diary_entry.mark_task_as_complete(task)
