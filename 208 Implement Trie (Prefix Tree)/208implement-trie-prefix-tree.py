class Tnode:
    def __init__(self):
        self.end=False
        self.children={}

class Trie:

    def __init__(self):
        self.root=Tnode()

    def insert(self, word: str) -> None:
        
        node=self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch]=Tnode()
            node=node.children[ch]
        
        node.end=True


    def search(self, word: str) -> bool:

        node=self.root

        for ch in word:
            if ch in node.children:
                node=node.children[ch]
            else:
                return False
        
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        
        node=self.root

        for ch in prefix:
            if ch in node.children:
                node=node.children[ch]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)