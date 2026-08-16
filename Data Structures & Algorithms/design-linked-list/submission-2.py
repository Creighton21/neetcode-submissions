class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.prev = prev
        self.next = next
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        k = 0
        while current:
            if k == index:
                return current.val
            current = current.next
            k += 1
        return - 1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, self.head, None)
        if self.size == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
        self.head = new_node
        self.size = self.size + 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val, None, self.tail)
        if self.size == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size = self.size + 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)

        if index == self.size:
            return self.addAtTail(val)
        
        if index > self.size or index < 0:
            return

        previous = self.head

        k = 0
        while previous:
            if k == index-1:
                new_node = ListNode(val, previous.next, previous)
                if previous.next:
                    previous.next.prev = new_node
                previous.next = new_node
                self.size = self.size + 1
                return
            previous = previous.next
            k += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            self.size = self.size - 1
            return

        if index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            self.size = self.size - 1
            return
        
        k = 0
        current = self.head
        while current:
            if k == index:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                self.size -= 1
                return
            current = current.next
            k += 1