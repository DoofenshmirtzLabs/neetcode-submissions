# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.res=True
        def dfs(root):
            if not root:
                return 0
            
            left=dfs(root.left)
            right=dfs(root.right)
            print('node:',root.val)
            print('right-left',abs(right-left))
            if abs(right-left)>1:
                self.res=False

            return max(left,right)+1
        
        dfs(root)
        return self.res
