def task_text_checker(text):
    if '#TODO' in text:
        return True
    else:
        return False