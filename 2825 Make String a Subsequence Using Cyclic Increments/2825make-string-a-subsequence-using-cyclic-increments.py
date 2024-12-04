class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        hmap = {chr(i): chr((i - 97 + 1) % 26 + 97) for i in range(97, 123)}
        
        cnt=0
        n=len(str2)

        for c in str1:
            if c==str2[cnt] or hmap[c]==str2[cnt]:
                cnt+=1
            
            if cnt==n:
                return True

        return False