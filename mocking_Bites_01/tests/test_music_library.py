from lib.music_library import *
from unittest.mock import Mock
def test_construct_music_library():
    music_library = MusicLibrary()
    assert music_library.tracks == []

def test_added_mock_tracks_are_in_tracks_list():
    music_library = MusicLibrary()
    track1 = Mock()
    track2 = Mock()
    track3 = Mock()
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.tracks == [track1, track2, track3]

def test_added_mock_tracks_are_found_by_search():
    music_library = MusicLibrary()
    matching_track = Mock()
    matching_track.matches.return_value = True
    not_matching_track = Mock()
    not_matching_track.matches.return_value = False
    music_library.add(matching_track)
    music_library.add(not_matching_track)
    assert music_library.search('Keyword') == [matching_track]

def test_added_mock_tracks_are_not_found_by_search():
    music_library = MusicLibrary()
    not_matching_track1 = Mock()
    not_matching_track1.matches.return_value = False
    not_matching_track2 = Mock()
    not_matching_track2.matches.return_value = False
    music_library.add(not_matching_track1)
    music_library.add(not_matching_track2)
    assert music_library.search('Keyword') == []




