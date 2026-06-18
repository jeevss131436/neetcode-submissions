# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)- 1)
        return pairs
    def quickSortHelper(self, pairs, s, e):
        if (e - s) + 1 <= 1:
            return 

        pivot = pairs[e] #Right Most

        left = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left += 1
        pairs[e] = pairs[left]
        pairs[left] = pivot
        self.quickSortHelper(pairs, s, left - 1) #left
        self.quickSortHelper(pairs, left + 1, e) #right
