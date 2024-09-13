class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        cnt=0
        allowed=set(allowed)

        for word in words:
            if set(word).issubset(allowed):
                cnt+=1

        return cnt