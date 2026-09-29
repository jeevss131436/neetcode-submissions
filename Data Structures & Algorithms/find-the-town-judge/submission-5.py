class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inbound = defaultdict(int)
        outbound = defaultdict(int)

        for src, dest in trust:
            inbound[dest] += 1
            outbound[src] += 1
        
        for i in range(1, n + 1):
            if outbound[i] == 0 and inbound[i] == n - 1:
                return i
                
        return -1