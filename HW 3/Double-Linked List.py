"""
UMass ECE 241   -   Advanced Programming
Homework #3     -   Fall 2019
hw3_q1_2019.py  -   Double-linked list
Complete the following methods in the code below!
search()
add()
size()
remove()
"""

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setPrev(self, newprev):
        self.prev = newprev

    def setNext(self, newnext):
        self.next = newnext


class OrderedDLList:
    def __init__(self):
        self.head = None
        self.tail = None

    def search(self, item):
        """complete the code necessary to allow to search for an item in the DLL"""
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        """complete the code necessary to allow to add an item in the DLL"""
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if current == None and previous == None:
            temp.setNext(self.head)
            self.head = temp
            self.tail = temp
        elif current == None:
            temp.setNext(current)
            self.tail = temp
            previous.setNext(temp)
            temp.setPrev(previous)
        elif previous == None:
            temp.setNext(current)
            current = temp
            current.getNext().setPrev(temp)
        else:
            temp.setNext(current)
            previous.setNext(temp)
            current.setPrev(temp)
            temp.setPrev(previous)

    def isEmpty(self):
        return self.head == None

    def size(self):
        """complete the code necessary to the size of the DLL"""
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def remove(self, item):
        """complete the code necessary to allow to remove an item in the DLL"""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
            current.getNext().setPrev(None)
        elif current.getNext() == None:
            previous.setNext(None)
            self.tail = previous
        else:
            previous.setNext(current.getNext())
            current.getNext().setPrev(current.getPrev())

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
mylist.add(44)


print(mylist.search(11))

mylist.printList()
print()
mylist.printRevList()

mylist.remove(11)
print()
mylist.printList()
print()
mylist.printRevList()