class SecretDiary:
    def __init__(self, diary):
        # diary is an instance of Diary
        self.diary = diary
        self.locked = True

    def read(self):
        # Raises the error "Go away!" if the diary is locked
        # Returns the diary's contents if the diary is unlocked
        # The diary starts off locked
        if self.locked == True:
            return 'Go away!'
        else:
            return self.diary.read()

    def lock(self):
        # Locks the diary
        # Returns nothing
        self.locked = True

    def unlock(self):
        # Unlocks the diary
        # Returns nothing
        self.locked = False


