class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        prefix=[]
        s=0
        cnt=0

        for num in nums:
            s+=num
            prefix.append(s)

        total=prefix[-1]

        for i in range(len(prefix)-1):
            if prefix[i]>=total-prefix[i]:
                cnt+=1

        return cnt