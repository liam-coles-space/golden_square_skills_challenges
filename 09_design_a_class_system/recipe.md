Describe the problem:

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

Design the class system: 

Diary
 - diary entries
 - add(diary_entry)
 - all_diary_entries()
    => [diary_entries...]
 - get_diary_entry_for_reading_speed_and_time(Minutes, WPM)
    => diary_entry
 - get_all_phone_number()
    => [phone_numbers...]
 - find_diary_entry_by_date(date)
    => diary_entry
 - mark_task_as_coomplete(date, task)   
______________________________________
|
| owns a list of
|
______________________________________
Diary entry
 - date
 - todos
 - phone numbers 
 - text 
 - text_word_count()
    => int
 - mark_task_as_complete(task)
_______________________________________
|                      |
| owns a list of       | owns a list of 
|                      |
_______________________________________
todo                   Phone Number
-task                  -number
-complete              -name 
-mark_as_complete()

class Diary:
    #User_facing properties:
    #    diary_entries: list of instances of DiaryEntry

    def __init__(self):
        pass

    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: instance of DiaryEntry
        # Side -effects:
        #   adds the diary_entry to the diary_entries property of the self object
        pass

    def all_diary_entries(self):
        # Returns:
        #   A list of all the diary_entry objects in the diary_entries propery
        pass
    
    def get_diary_entry_for_reading_speed_and_time(self, WPM, Minutes)
        # Parameters: 
        #   WPM: int
        #   Minutes: int
        # Returns:
        #   The diary entry object that has the text property that has the closest number of words to the WPM * Minutes

           
     