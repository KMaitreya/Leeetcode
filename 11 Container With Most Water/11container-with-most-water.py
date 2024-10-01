class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        vol, mvol=0, 0
        i, j=0, len(height)-1

        while i<j:
            vol=(j-i)*min(height[i], height[j])
            if height[i]<height[j]:
                i+=1 
            else:
                j-=1
            mvol=max(mvol, vol)
        
        return mvol