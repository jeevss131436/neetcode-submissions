# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, floor, ceiling):
            if root is None:
                return True
            if not (floor < root.val < ceiling):
                return False

            left = validate(root.left, floor, root.val)
            right = validate(root.right, root.val, ceiling)

            if left and right:
                return True
            return False
        return validate(root, float("-inf"), float("inf"))