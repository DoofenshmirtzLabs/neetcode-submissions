# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def dfs(root):
            if not root:
                return 0
            right=dfs(root.right)
            left=dfs(root.left)
            self.res=max(left+right,self.res)
            return max(right,left)+1
        dfs(root)
        return self.res
        