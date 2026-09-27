# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return self.goodNodesHelper(root, root.val)
        
    def goodNodesHelper(self, node, max_rn):
        if node is None:
            return 0
        if node.val >= max_rn:
            is_good = 1
        else:
            is_good = 0
        
        new_max = max(max_rn, node.val)
        left = self.goodNodesHelper(node.left, new_max)
        right = self.goodNodesHelper(node.right, new_max)

        return is_good + left + right

