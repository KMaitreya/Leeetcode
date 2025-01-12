class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        s=0
        cnt=0

        for x in nums:
            if x%6==0:
                s+=x
                cnt+=1
        
        if cnt==0:
            return 0
        return s//cnt