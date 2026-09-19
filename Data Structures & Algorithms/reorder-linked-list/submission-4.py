# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        secondHf = slow.next
        slow.next = None
        prev = None
        while secondHf:
            temp = secondHf.next
            secondHf.next = prev
            prev = secondHf
            secondHf = temp

        first = head
        secondHf = prev
        while secondHf:
            temp1 = first.next
            temp2 = secondHf.next
            first.next = secondHf
            secondHf.next = temp1
            first = temp1
            secondHf = temp2
         
