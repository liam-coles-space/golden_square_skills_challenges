def check_grammar(text):
    if len(text) == 0:
        return False
    if text[-1] in ['.', '!', '?' ] and text[0].isupper() == True:
        return True
    else:
        return False


