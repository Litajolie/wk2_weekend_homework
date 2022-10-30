import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Highway To Hell", "AC/DC")

    def test_song_has_title(self):
        self.assertEqual("Highway To Hell", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("AC/DC", self.song.artist)

if __name__ == '__main__':
    unittest.main()
