class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        nums.sort()
        nums.append("|")
        
        hmap={}
        cp, cnt=0, 1
        op=[]

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                cnt+=1
            else:
                if cnt not in hmap.keys():
                    hmap[cnt]=nums[cp:i+1]
                else:
                    hmap[cnt]=nums[cp:i+1]+hmap[cnt]
                cnt=1
                cp=i+1

        for key, value in sorted(hmap.items()):
            op+=value

        return op



        