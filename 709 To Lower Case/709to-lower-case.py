class Solution:
    def toLowerCase(self, s: str) -> str:

        s=list(s)
        op=""
        
        for i in range(len(s)):
            aci=ord(s[i])
            if aci>=65 and aci<=90:
                aci+=32
                op+=chr(aci)
            else:
                op+=s[i]

        return op