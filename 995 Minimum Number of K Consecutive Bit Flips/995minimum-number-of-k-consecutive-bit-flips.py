class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        flip = 0
        is_flipped = [0] * n  # This will track whether we have flipped at a given index
        result = 0

        for i in range(n):
            if i >= k:
                flip ^= is_flipped[i - k]  # Remove the effect of the flip k steps back

            if nums[i] == flip:
                if i + k > n:
                    return -1  # Not enough elements to flip
                result += 1
                flip ^= 1  # We perform a flip
                is_flipped[i] = 1  # Mark the current position as flipped

        return result