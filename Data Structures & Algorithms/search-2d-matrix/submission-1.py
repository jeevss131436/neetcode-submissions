class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols

            mid_val = matrix[row][col]

            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            elif mid_val < target:
                left = mid + 1

        return False

        
        
        
        
        # left = matrix[0][0]
        
        # right = matrix[rows][cols]

        # while left <= right:
        #     middle = matrix[rows//2][cols//2]

        #     if target < middle:
        #         if cols = 0:
        #             #Handle left side edge case. 
        #             right = matrix[rows/2 - 1]#[Cols value]
        #         else:
        #             right = matrix[rows/2][cols/2 - 1]
        #     elif target > middle:
        #         #Handle right side ewdgecase
        #         else:
        #             left = matrix[rows/2][cols/2 + 1]
        #     else:
        #         return True
        # return False