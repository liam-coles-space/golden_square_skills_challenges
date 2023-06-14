from lib.task_tracker import *

def test_task_list_initialised():
    task_tracker = TaskTracker()
    assert task_tracker.task_list == []

def test_add_tasks_to_list():
    task_tracker = TaskTracker()
    task_tracker.add_task('Brush teeth')
    task_tracker.add_task('Walk dog')
    assert task_tracker.task_list == ['Brush teeth', 'Walk dog']

def test_list_tasks():
    task_tracker = TaskTracker()
    task_tracker.add_task('Brush teeth')
    task_tracker.add_task('Walk dog')
    assert task_tracker.list_tasks() == ['Brush teeth', 'Walk dog']

def test_complete_task_removes_task_from_list():
    task_tracker = TaskTracker()
    task_tracker.add_task('Brush teeth')
    task_tracker.add_task('Walk dog')
    task_tracker.complete_task('Brush teeth')
    assert task_tracker.list_tasks() == ['Walk dog']
