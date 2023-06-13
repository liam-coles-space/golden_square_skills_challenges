User story:
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

def task_text_checker(text):
    """Check for '#TODO' in string

    Parameters:
        text: a string containing words (eg. 'I am string with #TODO in it')

    Returns:
        boolean value (E.g. True if string contains '#TODO', False if it does not)

    Side effects:
        None
    
Examples:

Given a empty string
It returns False
"""
task_text_checker("") => False

"""
Given a string containing '#TODO'
It returns True
"""
task_text_checker('I am string with #TODO in it') => True

"""
Given a string not containing '#TODO'
It returns False
"""
task_text_checker('I am string, hhoray') => False

"""
Given a string not containing '#TODO' but does contain 'TODO'
It returns False
"""
task_text_checker('I am TODO string, hhoray') => False
