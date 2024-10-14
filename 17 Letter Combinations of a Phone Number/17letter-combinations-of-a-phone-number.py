class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hmap={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }


        res=[]
        sub=[]
        n=len(digits)

        def backtrack(i):
            
            if i>=n:
                res.append("".join(sub))
                return

            for j in range(len(hmap[digits[i]])):
                sub.append(hmap[digits[i]][j])
                backtrack(i+1)
                sub.pop()

        if digits:
            backtrack(0)

        return res