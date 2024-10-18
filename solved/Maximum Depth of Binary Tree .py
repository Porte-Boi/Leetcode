class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def maxDepth(self, root: TreeNode) -> int:
        self._maxDepth_helper(root)
        return 
    
    def maxDepth_helper(self, node= TreeNode) -> int:
        if node is None:
            return 0
        
        left_depth =self.maxDepth_helper(node.left)
        right_depth =self.maxDepth_helper(node.right)
        return max(left_depth, right_depth) + 1
