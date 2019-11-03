"""
UMass ECE 241 - Advanced Programming
Project #1     Fall 2019
Song.py - Song class
"""

class Song:

    """
    Intial function for Song object.
    parse a given songRecord string to song object.
    For an example songRecord such as "0,Qing Yi Shi,Leon Lai,203.38893,5237536"
    It contains attributes (ID, title, artist, duration, trackID)
    """
    def __init__(self, songRecord):
        songRecord = songRecord.split(',')     # splits the string passed in to the Song Class by the load library at each ','
        self.ID = songRecord[0]             # assigns first item to the song ID parameter
        self.title = songRecord[1]          # assigns first item to the song title parameter
        self.artist = songRecord[2]         # assigns first item to the song artist parameter
        self.duration = songRecord[3]       # assigns first item to the song duration parameter
        self.trackID = songRecord[4]        # assigns first item to the song trackID parameter

    def toString(self):
        return "Title: " + self.title + ";  Artist: " + self.artist


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':

    sampleSongRecord = "0,Qing Yi Shi,Leon Lai,203.38893,5237536"
    sampleSong = Song(sampleSongRecord)
    print(sampleSong.toString())