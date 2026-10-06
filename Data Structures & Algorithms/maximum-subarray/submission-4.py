class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        best = curSum
        for num in nums[1::]:
            curSum = max(num, curSum + num)
            best = max(curSum, best)
        return best