# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, floor, ceiling):
            if not node:
                return True
            if not (floor < node.val < ceiling):
                return False
            return (validate(node.left, floor, node.val) and validate(node.right, node.val, ceiling))
        return validate(root, float("-inf"), float("inf"))