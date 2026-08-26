class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numStep = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numStep:
                return [numStep[complement], i]
            numStep[nums[i]] = i
        return []