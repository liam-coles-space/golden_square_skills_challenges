class DiaryEntry:
        # User_facing properties:
        #   text: string value
        #   date: value in format dd-mm-yyyy
        #   todos : list of Todo objects 
        #   phone_numbers: list of PhoneNumber objects 
        
    def __init__(self, date, text, todos, phone_numbers):
        self.date = date
        self.text = text
        self.todos = todos
        self.phone_numbers = phone_numbers

    def word_count(self):
        # Returns:
        #   int value representing number of words in text property of object
        return len(self.text.split())

    def mark_task_as_complete(self, task):
        # Parameters:
        #   task: string value 
        # Side effects:
        #   Changes complete property in single Todo object in todos property to True
        pass