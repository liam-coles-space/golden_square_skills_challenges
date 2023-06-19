from lib.todo import *

def test_construct_todo():
    todo = Todo('Shopping')
    assert todo.task == 'Shopping'
    assert todo.complete == False

def test_mark_as_complete_changes_complete_to_True():
    todo = Todo('Shopping')
    todo.mark_as_complete()
    assert todo.task == 'Shopping'
    assert todo.complete == True
