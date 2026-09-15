# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        a,b = head, head
        
        while a and a.next != None:
            a = a.next.next
            if a == b:
                return True
            b = b.next
        return False