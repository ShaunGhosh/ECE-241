"""
UMass ECE 241   -   Advanced Programming
Homework #3     -   Fall 2019
hw3_q1_2019.py      -   Double-linked list
Complete the following methods in the code below!
search()
add()
size()
remove()
"""

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self,newdata):
        self.data = newdata

    def setPrev(self, newprev):
        self.prev = newprev

    def setNext(self,newnext):
        self.next = newnext


class OrderedDLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, item):
    """complete the code necessary to allow to search for an item in the DLL"""

    def add(self, item):
        """complete the code necessary to allow to add an item in the DLL"""

    def isEmpty(self):
        return self.head == None

    def size(self):
        """complete the code necessary to the size of the DLL"""

    def remove(self, item):
        """complete the code necessary to allow to remove an item in the DLL"""

    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

    def printRevList(self):
        current = self.tail
        while current != None:
            print(current.getData())
            current = current.getPrev()


mylist = OrderedDLList()
mylist.add(10)
mylist.add(15)
mylist.add(20)
mylist.add(11)

print(mylist.search(11))

mylist.printList()
print()
mylist.printRevList()

mylist.remove(20)
print()
mylist.printList()
print()
mylist.printRevList()