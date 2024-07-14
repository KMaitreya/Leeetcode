# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        lst, nlst=[], []
        node=head

        while node:
            lst.append(node.val)
            node=node.next

        n=len(lst)

        for i in range(n):
            nlst.append(lst[i])
            nlst.append(lst[n-i-1])
        
        nlst=nlst[:n]

        node=head

        for num in nlst:
            node.val=num
            node=node.next

