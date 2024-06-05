class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        sep = {}
        final = []
        n = len(words)

        for word in words:
            counter = {}
            for letter in word:
                if letter in counter:
                    counter[letter] += 1
                else:
                    counter[letter] = 1
            sep[word] = counter
        

        common_counts = sep[words[0]].copy()
        
        for word in words[1:]:
            word_count = sep[word]
            for char in list(common_counts.keys()):
                if char in word_count:
                    common_counts[char] = min(common_counts[char], word_count[char])
                else:
                    del common_counts[char]

        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)
        
        return result