import random
from Graph import Vertex
from SongLibrary import SongLibrary
import pprint

class ArtistConnections:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        if self.getVertex(t) not in self.vertList[f].getConnections():
            self.vertList[f].addNeighbor(self.getVertex(t), 1)
            if self.getVertex(f) not in self.vertList[t].getConnections():
                self.vertList[t].addNeighbor(self.getVertex(f), 0)

        else:
            self.getVertex(t).coArtists[self.getVertex(f)] = self.vertList[f].getWeight(self.getVertex(t))+1

    """
    Load the artist connections graph based on a given song database
    Add the edges based on the last column of the collaborative artists 

    """

    def load_graph(self, songLibrary):

        songLib = SongLibrary()
        songLib.loadLibrary(songLibrary)

        for n in range(0, len(songLib.songArray)):

            if songLib.songArray[n].artist not in self.vertList:
                self.addVertex(songLib.songArray[n].artist)
                self.vertList[songLib.songArray[n].artist].songs.append(songLib.songArray[n].title)
                for m in songLib.songArray[n].colabArtists:
                    self.addEdge(songLib.songArray[n].artist, m)
            else:
                self.vertList[songLib.songArray[n].artist].songs.append(songLib.songArray[n].title)

                for m in songLib.songArray[n].colabArtists:
                    self.addEdge(songLib.songArray[n].artist, m)

        return self.numVertices

    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    def search_artist(self, artist_name):
        numSongs = 0
        artistLst = []

        for n in self.vertList:
            if self.vertList[n].getId() == artist_name:
                for m in self.vertList[n].getConnections():
                    if m.getId() not in artistLst:
                        artistLst.append(m.getId())
            for q in self.vertList[n].getConnections():
                if q.getId() == artist_name:
                    if self.vertList[n].getId() not in artistLst:
                        artistLst.append(self.vertList[n].getId())
        numSongs = len(self.vertList[artist_name].songs)
        #print(self.vertList[artist_name].songs)
        return numSongs, artistLst

    """
        Return a list of two-hop neighbors of a given artist
        """

    def find_new_friends(self, artist_name):
        two_hop_friends = []

        coArtists = self.search_artist(artist_name)[1]

        for n in coArtists:
            coo = self.search_artist(n)[1]
            for m in coo:
                if m != artist_name:
                    if m not in two_hop_friends:
                        two_hop_friends.append(m)

        return two_hop_friends

    def recommend_new_collaborator(self, artist_name):
        artist = ""
        numSongs = 0
        print(self.vertList[artist_name].coArtists)
        Potential_collaborators = self.find_new_friends(artist_name)
        coArtists = self.search_artist(artist_name)[1]
        Weights = {}
        for n in Potential_collaborators:
            self.vertList[artist_name].getWeight()


        print(coArtists)
        print(Weights)
        #for n in Potential_collaborators:


        return artist, numSongs

if __name__ == '__main__':
   Artist = ArtistConnections()

   Artist.load_graph("TenKsongs_proj2.csv")
   print(Artist.graph_info())
   print(Artist.search_artist("Mariah Carey"))
   print(Artist.find_new_friends("Green Day"))
   #Artist.recommend_new_collaborator("Mariah Carey")
   print(" ")
