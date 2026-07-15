# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,maximum):
            if not root:
                return 0
            print(root.val,maximum)
            if root.val>=maximum:
                maximum=root.val
                return 1+dfs(root.left,maximum)+dfs(root.right,maximum)
            else:
                return dfs(root.left,maximum)+dfs(root.right,maximum)
        
        return dfs(root,maximum=-float('inf'))
