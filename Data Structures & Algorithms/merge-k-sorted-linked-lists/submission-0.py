# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #use heaps to keep track of 2 smallest heads and helper function to combine them both
        if not lists:
            return None
        if len(lists)==1:
            return lists


        heap=[]
        for idx,node in enumerate(lists):
            heapq.heappush(heap,(node.val,idx,node))
        
        while len(heap)>1:
            _,idx,current_node1=heapq.heappop(heap)
            _,_,current_node2=heapq.heappop(heap)
            #print(current_node1.val,current_node2.val)
            merged_node=self.mergetwolists(current_node1,current_node2)
            #print(merged_node)
            heapq.heappush(heap,(merged_node.val,idx,merged_node))

        _,_,res=heapq.heappop(heap)

        return res
    
    def mergetwolists(self,head1,head2):

        dummy=ListNode(-float('inf'))
        prev=dummy

        while head1 and head2 :

            if head1.val<=head2.val:
                prev.next=head1
                head1=head1.next
            else:
                prev.next=head2
                head2=head2.next
            prev=prev.next
        if head1:
            prev.next=head1
        if head2:
            prev.next=head2
        #print(dummy.next)
        return dummy.next
    
