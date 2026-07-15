# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs at every level keep track of the last node

        queue=deque([root])
        res=[]
        while queue:
            n=len(queue)
            right_most=TreeNode(float('inf'))
            for i in range(n):
                current_node=queue.popleft()

                if current_node:
                    right_most=current_node
                    queue.append(current_node.left)
                    queue.append(current_node.right)
            print(right_most.val)
            if right_most.val!=float('inf'):
                res.append(right_most.val)
        
        return res

            