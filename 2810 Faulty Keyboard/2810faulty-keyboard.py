class Solution:
    def finalString(self, s: str) -> str:
        
        temp=""

        for char in s:
            if char=="i":
                temp=temp[::-1]
            else:
                temp+=char

        return temp