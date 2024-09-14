# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node=head

        while node.next:
            nnode=ListNode(math.gcd(node.val, node.next.val))
            nnode.next=node.next
            node.next=nnode
            node=nnode.next

        return head
