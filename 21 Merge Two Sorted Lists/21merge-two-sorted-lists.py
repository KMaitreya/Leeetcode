# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def traverse(node):
            lst=[]
            while node:
                lst.append(node.val)
                node=node.next
            return lst

        nl=sorted(traverse(list1)+traverse(list2))[::-1]

        nhead=None

        for val in nl:
            nnode=ListNode(val)
            nnode.next=nhead
            nhead=nnode

        return nhead