from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                curr_val = board[r][c]
                if curr_val == ".":
                    continue
                if curr_val in rows[r]:
                    return False
                if curr_val in cols[c]:
                    return False
                if curr_val in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(curr_val)
                cols[c].add(curr_val)
                boxes[(r // 3, c // 3)].add(curr_val)
        return True
