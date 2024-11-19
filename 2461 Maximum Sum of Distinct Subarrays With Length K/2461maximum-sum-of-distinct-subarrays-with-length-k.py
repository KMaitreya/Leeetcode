# class Solution:
#     def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
#         queue=[]
#         mcnt=0

#         prev=nums[0]

#         queue.extend(nums[:k])

#         for i in range(len(nums)-k):
#             queue.pop(0)
#             if nums[i+k] not in queue:
#                 mcnt=max(mcnt, sum(nums[i+1:i+k+1]))
#             queue.append(nums[i+k])
#         return mcnt
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0
        begin = 0
        end = 0
        num_to_index = {}

        while end < len(nums):
            curr_num = nums[end]
            last_occurrence = num_to_index.get(curr_num, -1)
            # if current window already has number or if window is too big, adjust window
            while begin <= last_occurrence or end - begin + 1 > k:
                current_sum -= nums[begin]
                begin += 1
            num_to_index[curr_num] = end
            current_sum += nums[end]
            if end - begin + 1 == k:
                ans = max(ans, current_sum)
            end += 1
        return ans