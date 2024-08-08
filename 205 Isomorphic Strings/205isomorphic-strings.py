class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        if len(set(s))!=len(set(t)):
            return False
        
        hmap={}

        for chars, chart in zip(s, t):
            if chars in hmap.keys():
                if hmap[chars]!=chart:
                    return False 
            else:
                hmap[chars]=chart

        return True
