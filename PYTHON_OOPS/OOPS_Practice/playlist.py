# Write a Python program that defines a Song class and a Playlist class. 
# The Playlist should support adding songs, removing songs by title, and shuffling the order of the playlist randomly.

import random
class Song:
    # Constructor method:-
    def __init__(self,name):
        self.name=name
        pass

class Playlist:
    # song=Song()
    # Constructor method:-
    def __init__(self):
        pass

    def add_song(self,name):
        song=Song()
        self.name=name
        song.songs.append(self.name)
        print(f"Updated playlist:- {song.songs}")

    def remove_song(self,name):
        song=Song()
        self.name=name
        song.songs.remove(self.name)
        print(f"Updated playlist:- {song.songs}")

    def shuffle_playlist(self):
        song=Song()
        random_song=random.choice(song.songs)
        print("Reshuffled playlist")
        print(f"playing {random_song}")

spotify=Playlist()
spotify.add_song("Saiyarra")
spotify.add_song("Aaj se teri")
spotify.add_song("Mere Mehboob Qayamat Hogi")