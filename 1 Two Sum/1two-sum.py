class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        # for i in range(1, len(nums)):
        #     if nums[i-1]+nums[i]==target:
        #         print(i-1, i)
        #         return [i-1, i]
        #     if nums[i]+nums[i]>target:
        #         break

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i]+nums[j]==target and i!=j:
        #             return [i, j]

        hmap={}

        for i in range(len(nums)):
            if nums[i] in hmap.keys():
                return [hmap[nums[i]], i]
            hmap[target-nums[i]]=i

