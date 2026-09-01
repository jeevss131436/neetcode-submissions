from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if board[r][c] == ".":
                    continue
                if value in rows[r]:
                    return False
                if value in cols[c]:
                    return False
                if value in boxes[(r//3, c//3)]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[(r//3, c//3)].add(value)
        return True