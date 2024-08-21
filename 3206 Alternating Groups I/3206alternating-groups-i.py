class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        cnt=0
        presets=[[0, 1, 0], [1, 0, 1]]
        colors+=colors[:2]

        for i in range(len(colors)-2):
            if colors[i:i+3] in presets:
                cnt+=1

        return cnt