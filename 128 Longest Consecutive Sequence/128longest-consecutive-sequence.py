class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums==[]:
            return 0
        
        nums=sorted(list(set(nums)))
        cnt, mcnt=0, 0

        for i in range(1, len(nums)):

            if nums[i]-nums[i-1]==1:
                cnt+=1
            else:
                if cnt>mcnt:
                    mcnt=cnt
                cnt=0
        
        if cnt>mcnt:
            mcnt=cnt

        return mcnt+1