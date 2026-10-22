# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next

        if values == values[::-1]:
            return True
        return False