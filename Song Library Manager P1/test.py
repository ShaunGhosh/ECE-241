
from Song import Song
from AVL_tree import AvlTree
import random
import time


class SongLibrary:
    """
    Intialize your Song library here.
    You can initialize an empty songArray, empty BST and
    other attributes such as size and whether the array is sorted or not

    """

    def __init__(self):
        self.songArray = list()
        self.songBST = None
        self.isSorted = False
        self.size = 0

    """
    load your Song library from a given file. 
    It takes an inputFilename and store the songs in songArray
    """

    def loadLibrary(self, inputFilename):
        songfile = open(inputFilename,"r")
        for aline in songfile:
            self.songArray.append(Song(aline))
            self.size += 1

        songfile.close()

    def buildBST(self):
        self.songBST = AvlTree()
        for i in range(len(self.songArray)):
            self.songBST.put(self.songArray[i].title, self.songArray[i])


    """
    Implement a search function for a query song (title) in the songBST.
    Return the song information string
    (After you find the song object, call the toString function)
    or None if no such song is found.
    """

    def searchBST(self, query):
        found = False
        current = self.songBST.root
        while not found and current is not None:
            if current.key == query:
                found = True
                print(self.songBST[current.key].toString())
            elif current.key > query:
                current = current.hasLeftChild()
            else:
                current = current.hasRightChild()
        if found == True:
            return True
        else:
            return False
    """
    Linear search function.
    It takes a query string and attribute name (can be 'title' or 'artist')
    and return the number of songs found in the library.
    Return -1 if no songs is found.
    Note that, Each song name is unique in the database,
    but each artist can have several songs.
    """

    def linearSearch(self, query, attribute):
        found = 0
        if attribute == "artist":
            for n in range(0,len(self.songArray)):
                if query == self.songArray[n].artist:
                    found += 1
        if attribute == "title":
            for n in range(0,len(self.songArray)):
                if query == self.songArray[n].title:
                    found += 1
        if found > 0:
            return found
        else:
            return -1

    def quickSort(self):
        alist = self.songArray
        self.quickSortHelper(alist, 0, len(alist) - 1)
        self.isSorted = True

    def quickSortHelper(self, alist, first, last):
        if first < last:
            splitpoint = self.partition(alist, first, last)
            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)



    def partition(self, alist, first, last):
        pivotvalue = alist[first].title

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark].title <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark].title >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark].title
                alist[leftmark].title = alist[rightmark].title
                alist[rightmark].title = temp

        temp = alist[first].title
        alist[first].title = alist[rightmark].title
        alist[rightmark].title = temp

        return rightmark



if __name__ == '__main__':
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs.csv")
    print(songLib.linearSearch("Blind Blake","artist"))
    songLib.quickSort()
    print([x.title for x in songLib.songArray])
    print(songLib.libraryInfo())
    songLib = SongLibrary()
    songLib.buildBST()
    print(songLib.searchBST("Thriller"))
