class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        odd_counts = [1 if num % 2 != 0 else 0 for num in nums]
    
        # Dictionary to store the frequency of prefix sums
        prefix_sum_count = {0: 1}
        prefix_sum = 0
        result = 0
        
        # Iterate over the binary array
        for count in odd_counts:
            # Update the current prefix sum
            prefix_sum += count
            
            # If (prefix_sum - k) exists in the dictionary, it means there are some subarrays ending at the current index with exactly k odd numbers
            if (prefix_sum - k) in prefix_sum_count:
                result += prefix_sum_count[prefix_sum - k]
            
            # Update the prefix sum count in the dictionary
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1
        
        return result