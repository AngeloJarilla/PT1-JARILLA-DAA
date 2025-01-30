'''
JARILLA, ANGELO CHRISTIENE M.
1) Linked list:
A linked list is a type of data structure in which pointers are used to connect its nodes. Every node has two components: the data and a link or reference to the node after it in the sequence. LinkedLists enable flexible memory allocation, which makes it simple to add or delete elements without effecting others, in contrast to arrays, where elements are kept in a continuous block of memory. However, since you have to go through the list from the beginning, looking for an element may take longer.
'''

class Node:
    def __init__(self, dataval):
        self.data = dataval
        self.SecondNode = None

class LinkedList:
    def __init__(self):
        self.FirstNode = None

    def append(self, dataval):
        NewNode = Node(dataval)
        if not self.FirstNode:
            self.FirstNode = NewNode
            return
        LastNode = self.FirstNode
        while LastNode.SecondNode:
            LastNode = LastNode.SecondNode
        LastNode.SecondNode = NewNode

    def show(self):
        Current = self.FirstNode
        while Current:
            print(Current.data, end=" to ")
            Current = Current.SecondNode
        print("None")

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.show()

#Sorry for the CamelCase