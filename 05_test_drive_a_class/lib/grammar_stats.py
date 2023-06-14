class GrammarStats:
    def __init__(self):
        self.success_count = 0
        self.check_count = 0
  
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        self.check_count += 1
        if len(text) > 0 and text[-1] in ['.', '!', '?' ] and text[0].isupper() == True:
            self.success_count += 1
            return True
        else:
            return False
  
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.

        if self.check_count == 0:
            return 0
        success_rate = (self.success_count/self.check_count) * 100


        return success_rate