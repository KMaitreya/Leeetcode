class Solution:
    def vowel_counter(self, window: str) -> int:

        vowels="aeiouAEIOU"
        cnt=0

        for char in window:
            if char in vowels:
                cnt+=1
        
        return cnt

    def maxVowels(self, s: str, k: int) -> int:
        s=list(s)
        cnt=0
        vowels="aeiouAEIOU"

        window=s[0:k]

        for char in window:
            if char in vowels:
                cnt+=1

        mcnt=cnt

        for i in range(len(s)-k):
            window=s[i:i+k]
            if s[i+k] in vowels:
                cnt+=1
            if s[i] in vowels:
                cnt-=1
            if cnt>mcnt:
                mcnt=cnt

        return mcnt


            