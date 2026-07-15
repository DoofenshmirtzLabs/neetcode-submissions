# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #basic idea is to check if both the p and q are greater or lesser than root
        #else root is the ancestor of both p and q

        if (p.val < root.val and q.val <root.val):
            return self.lowestCommonAncestor(root.left,p,q)
        elif (p.val>root.val and q.val>root.val):
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root