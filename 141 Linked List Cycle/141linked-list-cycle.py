# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        while head:
            head.val=str(head.val)
            if head.val[-1]=="_":
                return True
            head.val=head.val+"_"
            head=head.next
        return False