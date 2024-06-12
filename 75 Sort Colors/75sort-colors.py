class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        two_index = len(nums)

        i = 0

        while i < two_index:
            if nums[i] == 0:
                nums.insert(zero_index, nums.pop(i))
                zero_index += 1
                i += 1  # move to the next element as we have handled the current one
            elif nums[i] == 2:
                two_index -= 1
                nums.insert(two_index, nums.pop(i))
            else:
                i += 1

                print(nums)
                