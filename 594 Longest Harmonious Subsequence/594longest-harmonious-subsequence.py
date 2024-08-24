class Solution:
    def findLHS(self, nums: List[int]) -> int:

        hmap={}

        for num in nums:
            hmap[num]=1+hmap.get(num, 0)

        mcnt, cnt=0, 0

        for key in hmap.keys():
            if key+1 in hmap.keys():
                cnt=hmap[key]+hmap[key+1]
                if cnt>mcnt:
                    mcnt=cnt

        return mcnt