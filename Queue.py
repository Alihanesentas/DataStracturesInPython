'''
Queue
As a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed first. A good example of the queue is any queue of consumers for a resource where the consumer that came first is served first.
'''
'''
Operations associated with queue are:

Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity: O(1)
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition  Time Complexity: O(1)
Front: Get the front item from queue  Time Complexity: O(1)
Rear: Get the last item from queue  Time Complexity: O(1)'''








queue = []

queue.append('g')
queue.append('f')
queue.append('g')

print("Initial queue")
print(queue)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print("\n Queue after removing elements")
print(queue)
#Implementation using collections.deque
from collections import deque

q = deque()
q.append('g')
q.append('f')
q.append('g')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Implementation using queue.Queue
from queue import Queue

# Initializing a queue
q = Queue(maxsize = 3)

# qsize() give the maxsize
# of the Queue
print(q.qsize())

# Adding of element to queue
q.put('g')
q.put('f')
q.put('g')

# Return Boolean for Full
# Queue
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())