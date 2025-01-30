'''
JARILLA, ANGELO CHRISTIENE M.
2) Queues:
Using Queue data can be managed and arranged. Like a line at a ticket counter, a queue operates on the First In, First Out (FIFO) principle, which states that the first element added is the first one deleted. In contrast, a stack adheres to the Last In, First Out (LIFO) principle, which states that when plates are stacked and unstacked, the last item added is the first one removed. A heap is a unique kind of tree-based data structure that is mostly used for effectively managing priorities, including rapidly determining which element is the smallest or largest.
'''

class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, dataval):
        self.list.append(dataval)

    def dequeue(self):
        if len(self.list) < 1:
            return None
        return self.list.pop(0)

    def show(self):
        print("Queue:", self.list)


InQueue = Queue()
InQueue.enqueue(1)
InQueue.enqueue(2)
InQueue.enqueue(3)
InQueue.show()
InQueue.dequeue()
InQueue.show()

#Sorry for the CamelCase