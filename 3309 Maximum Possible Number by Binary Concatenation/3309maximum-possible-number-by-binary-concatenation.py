class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        
        n1=int(str(bin(nums[0])[2:])+str(bin(nums[1])[2:])+str(bin(nums[2])[2:]), 2)
        n2=int(str(bin(nums[0])[2:])+str(bin(nums[2])[2:])+str(bin(nums[1])[2:]), 2)
        n3=int(str(bin(nums[1])[2:])+str(bin(nums[0])[2:])+str(bin(nums[2])[2:]), 2)
        n4=int(str(bin(nums[1])[2:])+str(bin(nums[2])[2:])+str(bin(nums[0])[2:]), 2)
        n5=int(str(bin(nums[2])[2:])+str(bin(nums[0])[2:])+str(bin(nums[1])[2:]), 2)
        n6=int(str(bin(nums[2])[2:])+str(bin(nums[1])[2:])+str(bin(nums[0])[2:]), 2)
        
        return max(n1, n2, n3, n4, n5, n6)