class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0;
        counter = 0
        for index in nums:
            if index == 1:
                counter += 1
                if counter > streak:
                    streak = counter
            if index == 0:
                counter = 0
            

        return streak
            
