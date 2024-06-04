class Solution:
    def reverseVowels(self, s: str) -> str:
        
        s=list(s)
        vowels=[]
        final=""
        allvowels="aeiouAEIOU"
        for i in range(len(s)):
            if s[i] in allvowels:
                vowels.append(s[i])
                s[i]='_'
                
        for i in range(len(s)):
            if s[i]=='_':
                s[i]=vowels.pop()
            final=final+''.join(s[i])              
        
        return final
  
