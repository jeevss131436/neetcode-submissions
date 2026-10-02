class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * (len(isConnected))
        provinceCount = 0

        def dfs(node):
            visited[node] = True

            for nei in range(len(isConnected)):
                if isConnected[node][nei] and not visited[nei]:
                    dfs(nei)
        
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                provinceCount += 1
        return provinceCount