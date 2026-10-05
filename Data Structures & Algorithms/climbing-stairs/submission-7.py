class Solution:
    def climbStairs(self, n: int) -> int:
        wun, two = 1, 1
        for i in range(n - 1):
                temp = wun
                wun += two
                two = temp
        return wun