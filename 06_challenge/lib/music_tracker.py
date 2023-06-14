class MusicTracker():

    def __init__(self):
        self.track_list = []
    
    def add_track(self, track):
        self.track_list.append(track)

    def display_track_list(self):
        return self.track_list