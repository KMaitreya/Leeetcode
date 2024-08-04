class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        op=[]
        
        for i in range(n):
            j=i
            for j in range(i, n):
                if j==i:
                    op.append(nums[j])
                else:
                    op.append(sum(nums[i:j+1]))

        op=sorted(op)

        return sum(op[left-1:right])%(pow(10, 9)+7)