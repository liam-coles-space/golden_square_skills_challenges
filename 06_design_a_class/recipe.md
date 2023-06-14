1. Describe the problem 
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the class interface
class TaskTracker:

    def __init__(self):
        #Parameters = none

        #Side effects:
        sets the task_list property of the self object to an empty list
        pass

    def add_task(self, task):
        #Parameters = task, a string

        #Returns = none

        #side effects:
        appends task to task_list property

    def list_tasks(self):
        #parameters = none

        #returns task_list property

        #side effects: 
        None

    def complete_task(self, task):
        #parameters = task, a string

        #return = none

        #side effects:
        remove task from task_list property
