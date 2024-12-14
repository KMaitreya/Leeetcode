# class Solution:
#     def continuousSubarrays(self, nums: List[int]) -> int:
        
#         l=0
#         cnt=0
#         mi, ma=nums[0], nums[0]
        

#         for r in range(len(nums)):

#             mi=min(mi, nums[r])
#             ma=max(ma, nums[r])

#             while ma-mi>2:
#                 l+=1
#                 if nums[l-1]==mi:
#                     mi=min(nums[l:r+1])
#                 if nums[l-1]==ma:
#                     ma=max(nums[l:r+1])

#             cnt+=r-l+1

#         return cnt

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Map to maintain sorted frequency map of current window
        freq = {}
        left = right = 0
        count = 0  # Total count of valid subarrays

        while right < len(nums):
            # Add current element to frequency map
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # While window violates the condition |nums[i] - nums[j]| ≤ 2
            # Shrink window from left
            while max(freq) - min(freq) > 2:
                # Remove leftmost element from frequency map
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # Add count of all valid subarrays ending at right
            count += right - left + 1
            right += 1

        return count


            
            