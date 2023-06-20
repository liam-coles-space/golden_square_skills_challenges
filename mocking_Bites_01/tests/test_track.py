from lib.track import *

def test_construct_track():
    track = Track('Title 1', 'Artist 1')
    assert track.title == 'Title 1'
    assert track.artist == 'Artist 1'

def test_matches_returns_true_if_keyword_in_track_title():
    track = Track('Horse', 'Artist 1')
    assert track.matches('Horse') == True

def test_matches_returns_true_if_keyword_in_track_artist():
    track = Track('Title 5', 'Horse artist')
    assert track.matches('Horse') == True

def test_matches_returns_false_if_keyword_not_in_track_artist_or_title():
    track = Track('Title 5', ' artist')
    assert track.matches('Horse') == False

