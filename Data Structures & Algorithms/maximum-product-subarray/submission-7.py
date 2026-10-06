class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = minProduct = maxProduct = nums[0]
        for i in nums[1:]:
            candidates = [i, minProduct * i, maxProduct * i]
            minProduct = min(candidates)
            maxProduct = max(candidates)
            best = max(best, maxProduct)
        return best