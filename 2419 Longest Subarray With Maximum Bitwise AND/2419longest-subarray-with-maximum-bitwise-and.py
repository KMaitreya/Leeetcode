class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        m=max(nums)
        mcnt, cnt=0, 0

        for num in nums:
            if num==m:
                cnt+=1
            else:
                if cnt>mcnt:
                    mcnt=cnt
                cnt=0

        return max(mcnt, cnt)