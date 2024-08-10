# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:


        node=head
        nhead=ListNode()
        curr=nhead

        while node:
            if node.val!=val:
                nnode=ListNode(node.val)
                curr.next=nnode
                curr=nnode
            node=node.next

        curr=nhead.next
        del head

        return nhead.next