class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        cnt=0
        m=list(magazine)
        rn=list(ransomNote)

        for i in range(len(rn)):
            for j in range(len(m)):
                if rn[i]==m[j]:
                    cnt+=1
                    m[j]="_"
                    break
                    
            if len(ransomNote)==cnt:
                return True
        return False