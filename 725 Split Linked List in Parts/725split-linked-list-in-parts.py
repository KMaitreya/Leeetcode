# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        node = head
        n = 0

        # Calculate the length of the linked list
        while node:
            n += 1
            node = node.next

        splits = []
        curr = head

        # Calculate base size of each part and remainder
        part_size = n // k
        remainder = n % k

        for i in range(k):
            node = curr
            cnt = 0

            # Determine the number of nodes in this part
            temp = part_size + (1 if i < remainder else 0)

            # Traverse the current part
            while cnt < temp - 1 and curr:
                curr = curr.next
                cnt += 1

            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            # Append the head of this part to the splits list
            splits.append(node)

        return splits

