from lib.todo import *

def test_construct_todo():
    todo = Todo('Shopping')
    assert todo.task == 'Shopping'
