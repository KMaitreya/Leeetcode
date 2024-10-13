# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def traverse(node):
            s=0
            i=0

            while node:
                s+=(10**i)*node.val
                node=node.next
                i+=1
            return s

        ln=ListNode()
        head=None

        for i in str(traverse(l1)+traverse(l2)):
            ln=ListNode(i)
            ln.next=head
            head=ln
        
        return head

        