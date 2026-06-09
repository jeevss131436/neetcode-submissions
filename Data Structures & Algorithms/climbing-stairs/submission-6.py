class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * (n+1)

        if n <= 3:
            return n
        steps[1], steps[2] = 1, 2
        
        for n in range(3, n+1):
            steps[n] = steps[n-1] + steps[n-2]
        return steps[-1]   




        
        # else:
        #     steps.append(self.climbStairs(n-2))
        #     steps.append(self.climbStairs(n-1))
        # return steps[-1]
