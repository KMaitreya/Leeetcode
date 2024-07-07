class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:


        
        # for i in range(k):
        #     print(s)
        #     s=s[1:]+s[0]

        k=k%len(s)

        return s[k:]+s[:k]