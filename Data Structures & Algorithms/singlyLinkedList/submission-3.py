class LinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        if curr is None:
            return -1
        for i in range(index):
            curr = curr.next
            if curr is None:
                return -1
        return curr.val

    def insertHead(self, val: int) -> None:
        new_head = self.Node(val)
        new_head.next = self.head
        self.head = new_head


    def insertTail(self, val: int) -> None:
        new_tail = self.Node(val)
        if self.head is None:
            self.head = new_tail
            return

        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_tail

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head

        for i in range(index - 1):
            curr = curr.next
            if curr is None:
                return False
        if curr.next is None:
            return False

        curr.next = curr.next.next
        return True

    def getValues(self) -> List[int]:
        curr = self.head
        values = []
        while curr != None:
            values.append(curr.val)
            curr = curr.next
        return values