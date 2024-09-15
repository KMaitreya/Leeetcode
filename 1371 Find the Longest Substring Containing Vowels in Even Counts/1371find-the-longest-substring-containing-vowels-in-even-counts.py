class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        # vcount=[]
        # cnt=0
        # vowels="AEIOUaeiou"

        # for char in s:
        #     if char in vowels:
        #         cnt+=1
        #     vcount.append(cnt)

        # print(vcount)
        vowel_to_bit = {'a': 1 << 0, 'e': 1 << 1, 'i': 1 << 2, 'o': 1 << 3, 'u': 1 << 4}
    
        # Mask to store the state of vowels, initially all are even (mask = 0)
        mask = 0
        # Dictionary to store the first occurrence of each mask value
        mask_to_index = {0: -1}
        max_len = 0
        
        for i, char in enumerate(s):
            # Update mask if the character is a vowel
            if char in vowel_to_bit:
                mask ^= vowel_to_bit[char]
            
            # Check if we have seen this mask before
            if mask in mask_to_index:
                # The length of the substring is the difference between the current index and
                # the first occurrence of this mask
                max_len = max(max_len, i - mask_to_index[mask])
            else:
                # Store the first occurrence of this mask
                mask_to_index[mask] = i
        
        return max_len
