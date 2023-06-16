# File: lib/vowel_remover.py

class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        text_length = len(self.text)
        for i in range(text_length-1,-1,-1):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            i += 1
        return self.text
    
remover = VowelRemover("aeiou")
result_no_vowels = remover.remove_vowels()
assert result_no_vowels == ""

