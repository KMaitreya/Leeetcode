class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap={}
        res=[]
        
        for s in strs:
            s1="".join(sorted(s))
            if s1 not in hmap.keys():
                hmap[s1]=[]
            hmap[s1].append(s)
            
        for key, value in hmap.items():
            res.append(value)

        return res