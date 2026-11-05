class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        ROWS = len(grid)
        COLS = len(grid[0])
        freshOranges = 0
        mins = 0
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshOranges += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while q and freshOranges > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row < 0 or col == len(grid[0]) or col < 0 or row == len(grid) or grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append([row, col])
                    freshOranges -= 1
            mins += 1
        if freshOranges == 0:
            return mins
        return -1