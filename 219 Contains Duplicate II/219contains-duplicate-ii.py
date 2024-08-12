class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if len(set(nums))==len(nums):
            return False

        for i in range(len(nums)):
            if nums[i] in nums[i-k:i]+nums[i+1:i+k+1]:
                return True

        return False