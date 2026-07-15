# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        if not root:
            return 0
        
        self.res=0
        self.counter=0
        def dfs(root,maxval):
            if not root:
                return 
            if root.val>=maxval:
                self.counter+=1
                maxval=root.val
            dfs(root.left,maxval)
            dfs(root.right,maxval)
            return 
        dfs(root,maxval=root.val)
        return self.counter
