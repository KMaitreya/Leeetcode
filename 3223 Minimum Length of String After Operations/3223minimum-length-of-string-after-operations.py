class Solution:
    def minimumLength(self, s: str) -> int:

        hmap={}
        cnt=0
        n=len(s)
    
        for char in s:
            hmap[char]=1+hmap.get(char, 0)

        for key, value in hmap.items():
            if value>=3:
                if value%2==0:
                    cnt+=value-2
                else:
                    cnt+=value-1

        return n-cnt
