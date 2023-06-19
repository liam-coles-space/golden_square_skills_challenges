class Todo:
        # User_facing properties:
        #   Task: string value

    def __init__(self, task):
        self.task = task
        self.complete = False

    def mark_as_complete(self):
        # Side effects: 
        #   changes complete property to True
        self.complete = True