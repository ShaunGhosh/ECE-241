"""
UMass ECE 241 - Advanced Programming
Project #1     Fall 2019
SongLibrary.py - SongLibrary class
"""

from .Song import Song
from .AVL_tree import AvlTree
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
        songfile = open(inputFilename, "r")          # Takes input filename, opens it in read mode
        for aline in songfile:                       # reads line by line and converts each line into a song object
            self.songArray.append(Song(aline))       # and then appends it to the songArray
            self.size += 1                           # increases the size paramater by one each time an item is appended
        songfile.close()                   # closes the file

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
            for n in range(0, len(self.songArray)):          # looks for the artist attribute in the list
                if query == self.songArray[n].artist:        # returns positive if found
                    found += 1
        if attribute == "title":
            for n in range(0, len(self.songArray)):            # looks for the title attribute in the list
                if query == self.songArray[n].title:         # returns positive if found
                    found += 1
        if found > 0:
            return found
        else:
            return -1

    """
    Build a BST from your Song library based on the song title. 
    Store the BST in songBST variable
    """

    def buildBST(self):
        self.songBST = AvlTree()                                 # creates a new AVL_tree object
        for i in range(len(self.songArray)):                     # goes through the sorted list and uses the put
            self.songBST.put(self.songArray[i].title, self.songArray[i]) # method to assign the key - value pair to each node


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
                found = self.songBST[current.key].toString()
                return found
            elif current.key > query:
                current = current.hasLeftChild()
            else:
                current = current.hasRightChild()
        if found == True:
            return True
        else:
            return None


    """
    Return song libary information
    """

    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)

    """
    Sort the songArray using QuickSort algorithm based on the song title.
    The sorted array should be stored in the same songArray.
    Remember to change the isSorted variable after sorted
    """

    def quickSort(self):
        alist = self.songArray                              # assign songArray list to the alist variable
        self.quickSortHelper(alist, 0, len(alist) - 1)      # calls the quicksort helper method to split the list
        self.isSorted = True                              # changes isSorted to True after quicksorting

    def quickSortHelper(self, alist, first, last):
        if first < last:                                             # conditions for getting out of the recursion loop
            splitpoint = self.partition(alist, first, last)      # splitpoint variable calls the partition method for the quicksort
            self.quickSortHelper(alist, first, splitpoint - 1)   # recursively calling quicksorting each half of the list
            self.quickSortHelper(alist, splitpoint + 1, last)    # to arrange in an ascending order of characters based on ASCII value

    def partition(self, alist, first, last):
        pivotvalue = alist[first].title                  # sets pivot value to title parameter of the songArray object

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark].title <= pivotvalue:  # the core quicksort algorithm
                leftmark = leftmark + 1

            while alist[rightmark].title >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark           # returns rightmark


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs.csv")
    songLib.quickSort()
    songLib.buildBST()
    print(songLib.libraryInfo())
    print(songLib.searchBST("ddd"))
    songlib2 = SongLibrary()
    songlib2.songArray = random.sample(songLib.songArray, 100)
    songlib2.quickSort()


# Timing the linear search
    start_time = time.perf_counter_ns()
    for i in range(0, len(songlib2.songArray)):
        songlib2.linearSearch(songlib2.songArray[i].title, "Artist")
    end_time = time.perf_counter_ns()
    function_time = (end_time - start_time)/1000000000
    print(f"Time for linear search = {function_time} seconds")

# Timing the BST building
    start_time = time.perf_counter_ns()
    for i in range(0, len(songlib2.songArray)):
        songlib2.buildBST()
    end_time = time.perf_counter_ns()
    function_time = (end_time - start_time) / 1000000000
    print(f"Time for building BST = {function_time} seconds")

# Timing the BST search
    start_time = time.perf_counter_ns()
    for i in range(0, len(songlib2.songArray)):
        songlib2.searchBST(songlib2.songArray[i].title)
    end_time = time.perf_counter_ns()
    function_time1 = (end_time - start_time) / 1000000000
    print(f"Time for BST search = {function_time} seconds")

