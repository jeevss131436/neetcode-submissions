# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(node, floor, ceiling):
            if node is None:
                return True
            if not (floor < node.val < ceiling):
                return False
            return (validity(node.left, floor, node.val) and validity(node.right, node.val, ceiling))    
        return validity(root, float("-inf"), float("inf"))

        


