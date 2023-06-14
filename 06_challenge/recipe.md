1. Describe the problem
    As a user
    So that I can keep track of my music listening
    I want to add tracks I've listened to and see a list of them.

2. Design the class interface

class MusicTracker:
    User facing properties = none

    def __init__(self):
        #parameters = none

        #side effects:
        sets the track_list property of the self object 
        pass

    def add_track(self, track):
        #parameters = a string representing a single track 

        #returns: none

        #side effects:
        appends track to the track_list property

    def list_tracks(self):
        #parameters = none

        #returns the track_list

        #side effects: none

3. Create examples of tests

Given an instance of MusicTracker 
an instance variable, track_list, has been initialised to an empty list

Given multiple tracks, 
#add_track will add tracks to the track_list property

Calling the list_tracks method 
returns track_list property





