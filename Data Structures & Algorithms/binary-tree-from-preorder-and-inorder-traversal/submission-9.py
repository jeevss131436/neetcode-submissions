class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0  # pointer into preorder, tracks the "next root" to use
        
        def helper(in_left, in_right):
            # in_left, in_right = inclusive bounds in `inorder` for this subtree
            if in_left > in_right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            mid = inorder_map[root_val]
            
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            
            return root
        
        return helper(0, len(inorder) - 1)