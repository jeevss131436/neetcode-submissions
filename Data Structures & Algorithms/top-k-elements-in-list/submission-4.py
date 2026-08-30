class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        buckets = []
        for i in range(len(nums) + 1):
            buckets.append([])
        
        for num in frequencies:
            count = frequencies[num]
            buckets[count].append(num)

        result = []
        i = len(buckets) - 1
        while i > 0:
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
            i -= 1
        return result