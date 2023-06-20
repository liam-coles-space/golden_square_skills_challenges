from lib.music_library import *
from lib.track import *

#Add three tracks and they are now in tracks list
def test_added_tracks_are_in_tracks_list():
    music_library = MusicLibrary()
    track1 = Track('title 1', 'Dog')
    track2 = Track('Dog', 'Artist2')
    track3 = Track('title3', 'artist3')
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.tracks == [track1, track2, track3]

#Add four tracks, search for keyword and returns correct track(s) based on keyword
def test_search_finds_tracks_based_on_keyword():
    music_library = MusicLibrary()
    track1 = Track('title 1', 'Dog')
    track2 = Track('Dog', 'Artist2')
    track3 = Track('title3', 'artist3')
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.search('Dog') == [track1, track2]

def test_search_does_not_find_tracks_based_on_keyword():
    music_library = MusicLibrary()
    track1 = Track('title 1', 'Dog')
    track2 = Track('Dog', 'Artist2')
    track3 = Track('title3', 'artist3')
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.search('Horese') == []
