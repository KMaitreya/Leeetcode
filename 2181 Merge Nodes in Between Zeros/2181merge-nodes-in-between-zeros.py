# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        current = dummy
        sum_val = 0
        
        while head:
            if head.val == 0:
                if sum_val != 0:
                    current.next = ListNode(sum_val)
                    current = current.next
                    sum_val = 0
            else:
                sum_val += head.val
            head = head.next
        
        return dummy.next

    # Helper function to convert list to linked list for testing
    def list_to_linkedlist(arr):
        dummy = ListNode(0)
        current = dummy
        for num in arr:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

    # Helper function to convert linked list to list for testing
    def linkedlist_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result