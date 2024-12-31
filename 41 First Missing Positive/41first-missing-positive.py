class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        i=1
        nums=set(nums)

        while nums:
            if i in nums:
                nums.remove(i)
            else:
                return i
            i+=1

        return i
