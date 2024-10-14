class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #return sorted(nums, reverse=True)[k-1]

        heapq.heapify(nums)

        for _ in range(len(nums)-k):
            heapq.heappop(nums)

        return nums[0]



