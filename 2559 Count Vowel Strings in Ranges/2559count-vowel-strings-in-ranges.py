class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        i=0
        vowel=set("aeiou")
        stash=[0]

        for word in words:
            if word[-1] in vowel and word[0] in vowel:
                i+=1
            stash.append(i)

        return [stash[e+1]-stash[s] for s, e in queries]

            
            