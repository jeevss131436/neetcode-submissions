class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range(len(nums)):
            complement_val = target - nums[i]
            if complement_val in numsMap:
                return [numsMap[complement_val], i]
            numsMap[nums[i]] = i

        return[]
                    