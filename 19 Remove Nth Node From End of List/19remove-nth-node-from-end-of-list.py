# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        lst=[]
        node=head
        
        while node:
            lst.append(node.val)
            node=node.next

        lst=lst[::-1][:n-1]+lst[::-1][n:]
        head=None
        
        for i in range(len(lst)):
            node=ListNode(lst[i])
            node.next=head
            head=node

        return head
