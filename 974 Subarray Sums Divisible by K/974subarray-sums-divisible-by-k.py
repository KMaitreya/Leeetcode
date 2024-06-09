class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = {0: 1}
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # Adjust remainder to be non-negative
            if remainder < 0:
                remainder += k
            
            # If remainder is already in the map, add its count to the result
            if remainder in remainder_count:
                count += remainder_count[remainder]
            
            # Update the count of this remainder in the map
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
        
        return count