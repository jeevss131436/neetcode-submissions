class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        provinceCount = 0

        def dfs(node):
            visited[node] = True
            for ngbr in range(len(isConnected)):
                if isConnected[ngbr][node] and not visited[ngbr]:
                    dfs(ngbr)

        for i in range(len(isConnected)):
            if visited[i] == False:
                dfs(i)
                provinceCount += 1
        return provinceCount