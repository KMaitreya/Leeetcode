class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        if s[0] in ")}]":
            return False

        for char in s:
            if char in "({[":
                stack.append(char)
            if char in ")}]":
                if len(stack)==0:
                    return False
                elif char==")" and stack[-1]=="(" or char=="}" and stack[-1]=="{" or char=="]" and stack[-1]=="[":
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True