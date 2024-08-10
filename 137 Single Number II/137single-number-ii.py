class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hmap={}

        for num in nums:
            if num in hmap.keys():
                hmap[num]+=1
            else:
                hmap[num]=1

        for key, value in hmap.items():
            if value==1:
                return key

