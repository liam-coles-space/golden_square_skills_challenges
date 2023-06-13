
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


def calculate_reading_time(text)
    """"Calculates how many minutes it will take to read a string

        Parameters: 
            text: a string containing words (e.g. "I am an introduction to a book")

        Returns: 
            a float value to 1 decimal places

        Side effects:
            This function doesn't print anything or have any other side-effects

"""
Given a empty string 
It returns a float of 0.0
"""
calculate_reading_time("") => 0.0

"""
Given a string containing text with 20 words 
It returns a float of 0.1
"""
calculate_reading_time(20 Words here) => 0.1

"""
Given a string containing text with 450 words
It returns a float of 2.3
calculate_reading_time(450 Words here) => 2.3

"""
"""

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

"""
def check_grammar(text)
    """Confirms that a given string starts with a capital letter and ends with a full stop, exclamation point or question mark

    Parameters:
        a string containing words ("I am a sentence of words.)

    Return: 
        a boolean value, false for failing verification, True for passing verification

"""
Given an empty string
It returns False
"""
check_grammar(")

"""
Given a string that starts with an uppercase character and ends with a full stop
It returns True
"""
check_grammar("I am a sentence that should verify.")

"""
Given a string that starts with an uppercase character and ends with a exclamation point
It returns True
"""
check_grammar("Me am a happy text that should verify!")

"""
Given a string that starts with an uppercase character and ends with a question mark
It returns True
"""
check_grammar("You are a questioning text that should verify?")

"""
Given a string that starts with a lower case character that ends with suitable sentence ending punctuation-mark
It returns False
"""
check_grammar("you are a questioning text that should not verify?")
check_grammar("i am a text that should not verify.")
check_grammar("we are a text that should not verify!")

"""
Given a string that starts with a Upper case character that doe not end with suitable sentence ending punctuation-mark
It returns False
"""
check_grammar("This text should not return true")

"""
Given a string that starts with a lower case character that doe not end with suitable sentence ending punctuation-mark
It returns False
"""
check_grammar("any text like this should not return true")




    



    

