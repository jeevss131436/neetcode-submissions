class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.left 

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zeroes = students.count(0)
        ones = students.count(1)
        for s in sandwiches:
            if s == 0:
                if zeroes == 0:
                    return zeroes + ones
                zeroes -= 1
            else:
                if ones == 0:
                    return zeroes + ones
                ones -= 1
        return 0