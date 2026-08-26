class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinctSet = {}
        for i in range(len(nums)):
            if nums[i] in distinctSet:
                return True
            distinctSet[nums[i]] = i
        return False