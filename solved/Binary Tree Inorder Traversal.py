

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> int:
        res = []
        self._preorder_helper(root, res)
        return res
    
    def _preorder_helper(self, node = TreeNode, res = int):
        if not node:
            return
        res.append(node.val)
        self._preorder_helper(node.left, res)
        self._preorder_helper(node.right, res)