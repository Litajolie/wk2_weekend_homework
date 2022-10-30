from unicodedata import name


class Guest:
    def __init__(self,name,song):
        self.name = name
        self.favourite_song = song
# where is 2 coming from ? needs 4 arguements error?
    def cheer(self,songs):
