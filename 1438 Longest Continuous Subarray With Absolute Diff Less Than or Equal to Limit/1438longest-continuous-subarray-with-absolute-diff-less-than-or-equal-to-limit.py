class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        max_d = deque()  # Deque to keep track of max elements
        min_d = deque()  # Deque to keep track of min elements
        left = 0
        result = 0
        
        for right in range(len(nums)):
            # Maintain the deque for the maximum values
            while max_d and nums[max_d[-1]] <= nums[right]:
                max_d.pop()
            max_d.append(right)
            
            # Maintain the deque for the minimum values
            while min_d and nums[min_d[-1]] >= nums[right]:
                min_d.pop()
            min_d.append(right)
            
            # If the difference between the current max and min values exceeds the limit
            while nums[max_d[0]] - nums[min_d[0]] > limit:
                left += 1
                # Remove the elements from the deques if they are out of the current window
                if max_d[0] < left:
                    max_d.popleft()
                if min_d[0] < left:
                    min_d.popleft()
            
            # Update the result with the size of the current valid window
            result = max(result, right - left + 1)
        
        return result