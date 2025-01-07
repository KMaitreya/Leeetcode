class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
        s, cnt=0, 0

        for num in nums:
            s+=num

            if s==0:
                cnt+=1

        return cnt