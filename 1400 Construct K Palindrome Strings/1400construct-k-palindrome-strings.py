class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        hmap={}
        odds=0

        if len(s)<k:
            return False

        for c in s:
            hmap[c]=1+hmap.get(c, 0)

        for key, value in hmap.items():
            if value%2!=0:
                odds+=1
            
        return odds<=k