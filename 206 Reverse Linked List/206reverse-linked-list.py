# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node=head
        nhead=None

        while node:
            nnode=ListNode(node.val)
            nnode.next=nhead
            nhead=nnode

            node=node.next
        
        return nhead

