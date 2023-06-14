class TaskTracker:

    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def list_tasks(self):
        return self.task_list