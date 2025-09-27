'''
A linked list is a linear data stracture, in which the elements are not 
stored at contiguous memory locations. The elements
in a linked list are linked using pointer.  
'''
#Node Class
class Node:
    def __init__(self,data):
        self.data = data #assign data
        self.next = None #Initialize next as null
class LinkedList:
    def __init__(self):
        self.head = None 
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def insertAtFront(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    def insertAfter(self,data,key):
        curr = self.head
        while curr is not None:
            if curr.data == key:
                break
            curr = curr.next
        if curr is None:
            print("Node not found")
            return self.head
        newNode = Node(data)
        newNode.next = curr.next
        curr.next = newNode
    def insertBefore(self,data,key):
        if self.head  == None:
            return None
        if self.head.data == key:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
            return 
        prev = self.head
        curr = self.head.next
        while curr is not None and curr.data !=key:
            prev = curr
            curr = curr.next 
        if curr is None:
            print("Key not found!")
            return 
        newNode = Node(data)
        newNode.next = curr
        prev.next = newNode
    def insertPos(self,pos,val):
        if pos < 1:
            return self.head
        if pos == 1:
            newNode = Node(val)
            newNode.next = self.head
            return newNode
        curr = self.head
        for i in range(1,pos-1):
            if curr is None:
                return self.head
            curr = curr.next
        if curr is None:
            return self.head
        newNode = Node(val)
        newNode.next = curr.next 
        curr.next = newNode
        return self.head
    def insertAtLast(self,data):
        newNode = Node(data)
        if self.head is None:
            return newNode
        last = self.head

        while last.next is not None:
            last = last.next 
        last.next = newNode
        return self.head
    def deleteHead(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next 
        temp = None
        return self.head
    def deletePos(self,pos):
        temp = self.head
        if pos == 1:
            self.head = temp.next 
            return self.head
        
        prev = None
        for i in range(1,pos):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return self.head
    def deleteLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return None
        secondLast = self.head
        while secondLast.next.next is not None:
            secondLast = secondLast.next
        secondLast.next = None
        return self.head
    

    



    
list = LinkedList()
list.head = Node(1)
second = Node(2)
third = Node(3)

'''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third

    list.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | None |     | 2 | None |     | 3 | None |
    +----+------+     +----+------+     +----+------+
    '''
list.head.next = second
'''
    Now next of first Node refers to second. So they
    both are linked.

    list.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | null |     | 3 | null |
    +----+------+     +----+------+     +----+------+
'''
second.next = third
'''
    Now next of second Node refers to third. So all three
    nodes are linked.

    list.head     second             third
        |             |                 |
        |             |                 |
    +----+------+     +----+------+     +----+------+
    | 1 | o-------->| 2 | o-------->| 3 | null |
    +----+------+     +----+------+     +----+------+
    '''
if __name__ == '__main__':
    list = LinkedList()
    list.head = Node(1)
    second =Node(2)
    third = Node(3)
    list.head.next = second
    second.next = third
    data = 12
    list.insertAtFront(data)
    data,key = 2,3
    list.insertAfter(data=data,key=key)
    data,key = 6,2
    list.insertBefore(data=data,key=key)
    pos,val = 2,13
    list.insertPos(pos=pos,val=val)
    list.insertAtLast(14)
    list.deleteHead()
    list.deletePos(3)
    list.deleteLast()
    list.printList()