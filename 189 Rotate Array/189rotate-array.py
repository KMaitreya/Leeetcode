class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=k%len(nums)
        for i in range(r):
            nums[:0]=nums[-1:]
            del nums[-1:]
        
        
        