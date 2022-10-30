import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Highway to Hell", "AC/DC")
        self.song_2 = Song("The Clansman", "Iron Maiden")
        self.song_3 = Song("Ace of Spades", "Motorhead")

        self.songs = [self.song_1, self.song_2, self.song_3]

        self.jack = Guest("Jack", self.song_1)
        self.victor = Guest("Victor", self.song_2)
        self.isa = Guest("Isa", self.song_3)

        self.guests = [self.jack, self.victor, self.isa]

        self.winston = Guest("Winston", self.song_2)
        self.room = Room("The Metal Room")

    def test_room_has_name(self):
        self.assertEqual("The Metal Room", self.room.name)

    def test_room_has_no_guests_at_start(self):
        self.assertEqual(0, self.room.number_of_guests())

    def test_room_has_no_songs_at_start(self):
        self.assertEqual(0, self.room.number_of_songs())

    def test_can_check_in_guest(self):
        self.room.check_in_guest(self.victor)
        self.assertEqual(1, self.room.number_of_guests())

    def test_can_check_guest_out(self):
        self.room.check_in_guest(self.victor)
        self.room.check_out_guest(self.victor)
        self.assertEqual(0, self.room.number_of_guests())

    def test_can_add_song_to_room(self):
        song = Song("The Number of the Beast", "Iron Maiden")
        self.room.add_song(song)
        self.assertEqual(1, self.room.number_of_songs())

    def test_cheers_for_guests_fave_song(self):
        self.room.check_in_guest(self.winston)
        songs = self.songs
        self.assertEqual("Whoo Hoo!", self.room.guests[0].cheer(songs))


if __name__ == '__main__':
    unittest.main()
