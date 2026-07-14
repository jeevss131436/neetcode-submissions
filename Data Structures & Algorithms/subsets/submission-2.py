class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        subsets_without_first = self.subsets(nums[1:])
        result = []

        for subset in subsets_without_first:
            result.append(subset)
            result.append([nums[0]] + subset)
        return result