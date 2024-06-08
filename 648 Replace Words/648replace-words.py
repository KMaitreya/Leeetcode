class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        root_set = set(dictionary)
    
        # Split the sentence into words
        words = sentence.split()
        
        # Function to find the shortest root for a given word
        def find_root(word):
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in root_set:
                    return prefix
            return word
        
        # Replace each word in the sentence with the shortest root
        replaced_words = [find_root(word) for word in words]
        
        # Join the replaced words to form the final sentence
        return ' '.join(replaced_words)