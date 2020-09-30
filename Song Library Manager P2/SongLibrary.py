
class Song:

    def __init__(self, songRecord):
        tokens = songRecord.split(',')
        if len(tokens) != 6:
            print("incorrect song record")
        else:
            self.title = tokens[1]
            self.artist = tokens[2]
            self.duration = tokens[3]
            self.trackID = tokens[4]
            self.colabArtists = tokens[5][:len(tokens[5])-1].split(';')



    def toString(self):
        return "Title: " + self.title + ";  Artist: " + self.artist


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
            self.size += 1

        songfile.close()                            # closes the file

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
        Sort the songArray using QuickSort algorithm based on the song title.
        The sorted array should be stored in the same songArray.
        Remember to change the isSorted variable after sorted
        """

    def quickSort(self):
        alist = self.songArray  # assign songArray list to the alist variable
        self.quickSortHelper(alist, 0, len(alist) - 1)  # calls the quicksort helper method to split the list
        self.isSorted = True  # changes isSorted to True after quicksorting

    def quickSortHelper(self, alist, first, last):
        if first < last:  # conditions for getting out of the recursion loop
            splitpoint = self.partition(alist, first, last)     # splitpoint variable calls the partition method for the quicksort
            self.quickSortHelper(alist, first, splitpoint - 1)  # recursively calling quicksorting each half of the list
            self.quickSortHelper(alist, splitpoint + 1,last)    # to arrange in an ascending order of characters based on ASCII value

    def partition(self, alist, first, last):

        pivotvalue = alist[first].artist  # sets pivot value to title parameter of the songArray object
        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark].artist <= pivotvalue:  # the core quicksort algorithm
                leftmark = leftmark + 1

            while alist[rightmark].artist >= pivotvalue and rightmark >= leftmark:
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

        return rightmark  # returns rightmark

    """
    Return song libary information
    """
    def libraryInfo(self):
        return "Size: " + str(self.size) + ";  isSorted: " + str(self.isSorted)


# WRITE YOUR OWN TEST UNDER THAT IF YOU NEED
if __name__ == '__main__':
    songLib = SongLibrary()
    songLib.loadLibrary("TenKsongs_proj2.csv")
    songLib.quickSort()
    ulist = []
    count =0
    for n in range(0,len(songLib.songArray)):
        if songLib.songArray[n].artist not in ulist:
            ulist.append(songLib.songArray[n].artist)
            count += 1

    pprint.pprint(ulist)
    print('count:'+ str(count))
    print(songLib.libraryInfo())

