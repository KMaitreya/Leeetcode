# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        critical_points = []
        index = 1
        prev, curr, next = head, head.next, head.next.next

        while next:
            if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
                critical_points.append(index)
            prev, curr, next = curr, next, next.next
            index += 1

        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float('inf')
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])

        max_distance = critical_points[-1] - critical_points[0]

        return [min_distance, max_distance]

    # Helper function to convert list to linked list for testing
    def list_to_linkedlist(arr):
        dummy = ListNode(0)
        current = dummy
        for num in arr:
            current.next = ListNode(num)
            current = current.next
        return dummy.next