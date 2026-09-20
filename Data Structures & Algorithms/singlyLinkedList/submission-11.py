class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    
    def get(self, index: int) -> int:
        # index out of bound
        if index >= self.length or index < 0:
            return -1

        # get from head
        if index == 0:
            return self.head.value

        # get from tail
        if index == self.length - 1:
            return self.tail.value

        # get from in between
        curr = self.head
        for i in range(index):
            curr = curr.next
        
        return curr.value
      
        

    def insertHead(self, val: int) -> None:
        node = Node(val)
        if self.length < 1: 
            self.head = node
            self.tail = node
            self.length = 1
        else:
            node.next = self.head
            self.head = node
            self.length += 1
        

    def insertTail(self, val: int) -> None:
        node =  Node(val)
        if self.length == 0:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.length += 1
        

    def remove(self, index: int) -> bool:
        # index is out of bound
        if index >= self.length or index < 0:
            return False

        # remove from head
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return True

        # remove from in between
        curr = self.head
        for i in range(index-1):
            curr = curr.next
            
        if index + 1 == self.length:
            curr.next = None
            self.tail = curr
        else:
            curr.next = curr.next.next
        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:
        listVal = []
        curr = self.head
        while curr:
            listVal.append(curr.value)
            curr = curr.next
        return listVal
        
