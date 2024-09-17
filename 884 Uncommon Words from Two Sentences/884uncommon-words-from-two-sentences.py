class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        s=s1.split()+s2.split()
        hmap={}
        op=[]
        
        for word in s:
            hmap[word]=1+hmap.get(word, 0)

        for key, value in hmap.items():
            if value==1:
                op.append(key)

        return op



