class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        def common_prefix_length(str1, str2):
            length = 0
            # Iterate over both strings, character by character
            for c1, c2 in zip(str1, str2):
                if c1 == c2:
                    length += 1
                else:
                    break
            return length

        # Sort both arrays based on their string representations
        arr1_sorted = sorted(map(str, arr1))
        arr2_sorted = sorted(map(str, arr2))
        
        max_length = 0
        
        i, j = 0, 0
        while i < len(arr1_sorted) and j < len(arr2_sorted):
            # Compare common prefix of current pair
            prefix_length = common_prefix_length(arr1_sorted[i], arr2_sorted[j])
            max_length = max(max_length, prefix_length)
            
            # Move the pointer of the array with the smaller string to minimize comparison
            if arr1_sorted[i] < arr2_sorted[j]:
                i += 1
            else:
                j += 1
        
        return max_length