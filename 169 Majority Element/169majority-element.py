class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hmap={}

        for num in nums:
            if num in hmap.keys():
                hmap[num]+=1
            else:
                hmap[num]=1

        for key, value in hmap.items():
            if value==max(hmap.values()):
                return key
            