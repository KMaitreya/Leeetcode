class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Find the intersection by taking the minimum of corresponding counts
        intersection = count1 & count2
        
        # Expand the intersection into a list
        result = []
        for num in intersection:
            result.extend([num] * intersection[num])
        
        return result