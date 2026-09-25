# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)
        return max(left, right)


        # elif root.left is None and root.right:
        #     depth = 1 + self.maxDepth(root.right)
        # elif root.left and root.right is None:
        #     depth = 1 + self.maxDepth(root.left)
        # else:
        #     depth = 1 + self.maxDepth(root.left)
        #     depth = 1 + self.maxDepth(root.right)
        # return depth