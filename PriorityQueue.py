'''
if datas are different proirty we use that, also extantion of the queue.
* An element with high priority is dequeued bedfore an element with low priporty.
* If two elements have the same prioryty thet are serverd according to their order in the queue.

'''

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) == 0
    def insert(self,data):
        self.queue.append(data)
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
    def deletemin(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item 
        except IndexError:
            print()
            exit()                                  
if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(122)
    myQueue.insert(123)
    myQueue.insert(2)
    myQueue.insert(332)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.deletemin())
    while not myQueue.isEmpty():
        print(myQueue.delete())
