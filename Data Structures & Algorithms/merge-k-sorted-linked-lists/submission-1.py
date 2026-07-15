# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        if len(lists)==0:
            return lists
        
        heap=[]

        for index,curr_node in enumerate(lists):

            heapq.heappush(heap,(curr_node.val,index,curr_node))
        
        while len(heap)>1:
            _,current_index,head1=heapq.heappop(heap)
            _,_,head2=heapq.heappop(heap)#smallest two nodes
            #print(head1.val,head2.val)
            output=self.mergetwolist(head1,head2)
            heapq.heappush(heap,(output.val,current_index,output))
        
        _,_,res=heapq.heappop(heap)

        return res






    def mergetwolist(self,head1,head2):

        dummy=ListNode()
        prev=dummy

        while head1 and head2:
           # print('head1,head2',head1.val,head2.val)
            if head1.val<=head2.val:
                #print('adding',head1.val)
                prev.next=head1
                head1=head1.next
            else:
                #print('adding',head1.val)

                prev.next=head2
                head2=head2.next
            prev=prev.next
            
        prev.next=head1 or head2

        return dummy.next





