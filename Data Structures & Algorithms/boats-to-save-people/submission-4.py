class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        boatCounter = 0

        while left <= right:
            remain = limit - people[right]
            right -= 1
            boatCounter += 1
            if left <= right and remain >= people[left]:
                left += 1
        return boatCounter
