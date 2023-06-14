from lib.music_tracker import *

def test_init_creates_track_list():
    music_tracker = MusicTracker()
    assert music_tracker.track_list == []

def test_add_tracks_to_list():
    music_tracker = MusicTracker()
    music_tracker.add_track("Walking on sunshine")
    music_tracker.add_track("Beat it")
    music_tracker.add_track("my favourite song")
    assert music_tracker.track_list == ["Walking on sunshine", "Beat it", "my favourite song"]

def test_display_track_list_returns_list():
    music_tracker = MusicTracker()
    music_tracker.add_track("Walking on sunshine")
    music_tracker.add_track("Beat it")
    music_tracker.add_track("my favourite song")
    assert music_tracker.display_track_list() == ["Walking on sunshine", "Beat it", "my favourite song"]