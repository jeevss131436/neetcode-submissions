# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidRange(self, node, low, high):
        if node is None:
            return True
        if low < node.val < high:
            return self.isValidRange(node.left, low, node.val) and self.isValidRange(node.right, node.val, high)
        return False

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidRange(root, float('-inf'), float('inf'))


    
