class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        output = []
        for i, n in enumerate(nums):
            difference = target - n
            if difference in numsMap:
                return [numsMap[difference], i]
            numsMap[n] = i
        return []