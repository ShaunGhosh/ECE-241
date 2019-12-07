import sys
from .Graph import Queue
from .Graph import Vertex
from .SongLibrary import SongLibrary

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

        if self.getVertex(t) not in self.vertList[f].getConnections():          # if the vertex t not in coArtists of f
            self.vertList[f].addNeighbor(self.getVertex(t), 1)                  # add edge between t and f with weight 1
            if self.getVertex(f) not in self.vertList[t].getConnections():      # if the vertex f not in coArtists of t
                self.vertList[t].addNeighbor(self.getVertex(f), 0)              # add edge with no weight

        else:
            self.getVertex(t).coArtists[self.getVertex(f)] = self.vertList[f].getWeight(self.getVertex(t))+1 #update weights if the Artists have more than one song together

    """
       Load the artist connections graph based on a given song database
       Add the edges based on the last column of the collaborative artists 

       """

    def load_graph(self, songLibrary):

        songLib = SongLibrary()             # create SongLibrary Object
        songLib.loadLibrary(songLibrary)    # load song library

        for n in range(0, len(songLib.songArray)): # loop through the entire song library

            if songLib.songArray[n].artist not in self.vertList: # if the vertex is not in the Graph
                self.addVertex(songLib.songArray[n].artist)      # create vertex
                self.vertList[songLib.songArray[n].artist].songs.append(songLib.songArray[n].title) # add the song to the songs attribute of the Vertex
                for m in songLib.songArray[n].colabArtists:      # loop through the coArtists attribute of the Vertex
                    self.addEdge(songLib.songArray[n].artist, m) # create the vertices when required and add the edges between the vertices of the artist and the coArtists
            else:
                self.vertList[songLib.songArray[n].artist].songs.append(songLib.songArray[n].title)  # just append the songs to the Vertices if the vertices already in the Graph

                for m in songLib.songArray[n].colabArtists:      # add edge for between each vertices that are already in the graph
                    self.addEdge(songLib.songArray[n].artist, m)

        return self.numVertices                  # return total vertices in the Graph

    """
    Return song library information
    """

    def graph_info(self):
        return "Vertex Size: " + str(self.numVertices)

    """
    Search the information of an artist based on the artist name
    Return a tuple (the number of songs he/she wrote, the collaborative artist list)

    """

    def search_artist(self, artist_name):
        numSongs = 0
        artistLst = []

        for n in self.vertList:                                     # loops through the graph to find the coArtists
            if self.vertList[n].getId() == artist_name:            # only if the vertex matches the artist name parameter
                for m in self.vertList[n].getConnections():      # loop through the connections of the vertex
                    if m.getId() not in artistLst:              # add neighboring artist to the artistLst if its not there already
                        artistLst.append(m.getId())
            for q in self.vertList[n].getConnections():                 # if the any vertex in the graph as a connection to the given artist
                if q.getId() == artist_name:                         # add the artist name to the coArtist list if its not there
                    if self.vertList[n].getId() not in artistLst:
                        artistLst.append(self.vertList[n].getId())
        numSongs = len(self.vertList[artist_name].songs)            # number of songs is equal to the length of the Songs list Parameter of a vertex

        return numSongs, artistLst

    """
    Return a list of two-hop neighbors of a given artist
    """

    def find_new_friends(self, artist_name):
        two_hop_friends = []

        coArtists = self.search_artist(artist_name)[1]   #find the connections using the search_artist method and using the 2nd element of the tuple

        for n in coArtists:                    # loop through ever coArtist and find their coArtists by calling the search_artist method again
            coco = self.search_artist(n)[1]    # using the 2nd element of the tuple i.e. the artists
            for m in coco:                     # looping through the connections of the connections
                if m != artist_name:           # because onE of the connections of the connections 2 hop would be the GIVEN vertex
                    if m not in two_hop_friends and m not in coArtists: #if the vertex doesn't already exist and not in coArtists
                        two_hop_friends.append(m)                       # append the vertices.artist


        return two_hop_friends

    """ 
    Search the information of an artist based on the artist name

    """

    def recommend_new_collaborator(self, artist_name):
        artist = ""
        numSongs = 0

        coArtist = self.search_artist(artist_name)      # get a list of coArtists using search_artist method
        Potential_collaborators = self.find_new_friends(artist_name)  #get a list of coArtist of coArtists using find_new_friends method
        Weights = {}   # initialize dictionary to store CoArtist - Weight and key - value pair

        for n in coArtist:         # loop through the coArtist
            for m in Potential_collaborators:  # loop through the coArtist of the coArtists to find the collaborations and the weights between them
                if Weights[self.getVertex(m)]:
                    Weights[self.getVertex(m)] = self.getVertex(m).getWeights(self.getVertex(n)) # add up the weights if there are more than one collaboration

         # suggests the best collaborators on the sum of the

        return artist, numSongs

    """
    Search the information of an artist based on the artist name
    """

    def shortest_path(self, artist_name):               # shortest path between each vertex and a given vertex using the Breadth first search
        path = {}
        for n in self.vertList:
            self.getVertex(n).dist = sys.maxsize
            self.getVertex(n).color = 'white'
            self.getVertex(n).pred = None
            self.getVertex(n).dist = 0
            self.getVertex(n).disc = 0
            self.getVertex(n).fin = 0
        self.getVertex(artist_name).setDistance(0)
        self.getVertex(artist_name).setPred(None)
        vertQueue = Queue()
        vertQueue.enqueue(self.vertList[artist_name])
        while (vertQueue.size() > 0):
            currentVert = vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')

            for n in self.vertList:                   #get the distance of each vertices based on their weights
                path[n] = self.getVertex(n).dist


        return path




# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    Artist = ArtistConnections()

    Artist.load_graph("TenKsongs_proj2.csv")
    print(Artist.graph_info())
    print(Artist.search_artist("Mariah Carey"))
    print(Artist.find_new_friends("Green Day"))
    # Artist.recommend_new_collaborator("Mariah Carey")
    print(Artist.shortest_path("Green Day"))


