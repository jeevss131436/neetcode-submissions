class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, n in enumerate(nums):
            remaining = target - n
            if remaining in numsMap:
                return [numsMap[remaining], i]
            numsMap[n] = i
        return []