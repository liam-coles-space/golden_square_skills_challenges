def calculate_reading_time(text):
    word_count = len(text.split(' '))
    return round(word_count/200, 1)
