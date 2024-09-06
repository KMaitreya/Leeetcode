# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        ## Method 1

        # node=ListNode(0)
        # node.next=head
        # curr=node

        # while curr.next:
        #     if curr.next.val in nums:
        #         curr.next=curr.next.next
        #     else:
        #         curr=curr.next
        # return node.next


        ## MEthod 2

        node=head
        lst=[]
        res=[]
        nums=set(nums)

        while node:
            lst.append(node.val)
            node=node.next

        nhead=ListNode()
        node=nhead

        for num in lst:
            if num not in nums:
                new=ListNode(num)
                node.next=new
                node=new

        return nhead.next