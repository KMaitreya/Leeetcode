class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        length=len(nums)
        
        if sum(nums[1:])==0:
            return 0
        
        for i in range(1,length-1):
            if sum(nums[0:i])==sum(nums[i+1:length]):
                return i
        
        if sum(nums[0:length-1])==0:
            return length-1
        
        return -1
        

    
            