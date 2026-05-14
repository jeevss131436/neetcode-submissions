class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        for index in range(len(ans)):
            if index < len(nums):
                ans[index] = nums[index]
            if index >= len(nums):
                ans[index] = nums[index - len(nums)]
        return ans