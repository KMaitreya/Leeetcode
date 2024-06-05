class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        final=[]
        n1=set(nums1)
        n2=set(nums2)

        final.append(list(n1-n2))
        final.append(list(n2-n1))
        
        return final
                