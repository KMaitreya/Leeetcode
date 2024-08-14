class Solution:
    

    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def countPairs(nums, mid):
            count = 0
            left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count
        
        nums.sort()  # Sort the array to use two-pointer technique
        low, high = 0, nums[-1] - nums[0]  # Minimum and maximum possible distances
        
        while low < high:
            mid = (low + high) // 2
            if countPairs(nums, mid) >= k:
                high = mid  # Look for smaller distances
            else:
                low = mid + 1  # Look for larger distances
        
        return low
