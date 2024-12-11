class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        # hmap={}
        # mcnt=0

        # for num in nums:
        #     for i in range(num-k, num+k+1):
        #         hmap[i]=hmap.get(i, 0)+1
        #         mcnt=max(mcnt, hmap[i])

        # return mcnt

        hmap = {}
        mcnt = 0

        # Update ranges in the frequency map
        for num in nums:
            # Increment the start of the range
            hmap[num - k] = hmap.get(num - k, 0) + 1
            # Decrement the end of the range
            hmap[num + k + 1] = hmap.get(num + k + 1, 0) - 1

        # Calculate the maximum frequency using prefix sum
        current_count = 0
        for key in sorted(hmap.keys()):
            current_count += hmap[key]
            mcnt = max(mcnt, current_count)

        return mcnt
