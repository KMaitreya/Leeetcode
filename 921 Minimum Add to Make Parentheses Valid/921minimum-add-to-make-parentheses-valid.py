class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack=[]
        cnt=0

        for x in s:
            if x=="(":
                stack.append(x)
            elif stack:
                if x==")" and stack[-1]=="(":
                    stack.pop()
            else:
                cnt+=1

        return len(stack)+cnt