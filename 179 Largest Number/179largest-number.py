class Solution:
    from functools import cmp_to_key
    def largestNumber(self, nums: List[int]) -> str:

        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0   # they are equal

        # Convert numbers to strings
        nums_str = list(map(str, nums))
        
        # Sort based on the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Join sorted numbers into a single string
        largest_num = ''.join(nums_str)
        
        # Handle the case where the largest number is "0" (e.g., nums = [0, 0])
        return '0' if largest_num[0] == '0' else largest_num
