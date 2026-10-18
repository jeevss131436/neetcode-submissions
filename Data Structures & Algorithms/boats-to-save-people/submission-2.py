class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left = 0
        right = len(people) - 1
        boatCounter = 0
        result = 0
        people.sort()

        while left <= right:
            remain = limit - people[right]
            right -= 1
            boatCounter += 1
            if left <= right and remain >= people[left]:
                left += 1
        return boatCounter

        
