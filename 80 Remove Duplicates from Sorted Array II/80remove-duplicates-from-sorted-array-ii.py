class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        temp={}
        for i in range(l):
            if temp.get(nums[i])==None:
                temp[nums[i]]=1
            elif temp[nums[i]]<2:
                temp[nums[i]]+=1
        result_list = []
        for key, value in temp.items():
            result_list.extend([key] * value)
        nums.clear()
        nums[:0]=result_list
        # cnt=1
        # k=0
        # for i in range(1,l):
        #     print(cnt, i)
        #     if nums[i]==nums[i-1]:
        #         cnt+=1
        #     elif nums[i]<nums[i-1]:
        #         break
        #     else:
        #         cnt=0
        #     if cnt==3:
        #         nums.append(nums[i])
        #         nums.remove(nums[i])
        #         k+=1
        #         if nums[i]==nums[i-1]:
        #             i-=1

        #     print(nums)

        return len(result_list)


        
        