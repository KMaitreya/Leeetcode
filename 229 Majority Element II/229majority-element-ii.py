class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        hmap={}
        n=len(nums)

        for num in nums:
            hmap[num]=hmap.get(num, 0)+1

        return [key for key, value in hmap.items() if value>n//3]        