class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited_islands = set()


        def dfs(i, j):
            if i == len(grid) or j == len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0 or (i, j) in visited_islands:
                return 0          

            visited_islands.add((i, j))

            a = dfs(i + 1, j)
            a += dfs(i - 1, j)
            a += dfs(i, j + 1)
            a += dfs(i, j - 1)
            return 1 + a

        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area, dfs(r, c))

        return area
        
