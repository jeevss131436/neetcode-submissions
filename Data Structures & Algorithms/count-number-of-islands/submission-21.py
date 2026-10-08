class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        islandCount = 0

        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == "1" and (r, c) not in visited:
                        visited.add((r, c))
                        q.append((r, c))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islandCount += 1
        return islandCount