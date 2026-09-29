class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited_islands = set()
        
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in visited_islands:
                return 0

            visited_islands.add((i, j))

            perimeter = 0
            perimeter += dfs(i, j + 1)
            perimeter += dfs(i, j - 1)
            perimeter += dfs(i + 1, j)
            perimeter += dfs(i - 1, j)

            return perimeter

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(r, c)