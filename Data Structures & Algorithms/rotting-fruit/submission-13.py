class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        mins = 0
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            mins += 1
        if fresh == 0:
            return mins
        else:
            return -1
