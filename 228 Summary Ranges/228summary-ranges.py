class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []
        
        temp=[]
        final=[]

        for num in nums:
            if not temp or num==temp[-1]+1:
                temp.append(num)
            else:
                if len(temp)>1:
                    final.append(str(temp[0])+"->"+str(temp[-1]))
                else:
                    final.append(str(temp[0]))
                temp=[num]

        if len(temp)>1:
            final.append(str(temp[0])+"->"+str(temp[-1]))
        else:
            final.append(str(temp[0]))

        return final
            