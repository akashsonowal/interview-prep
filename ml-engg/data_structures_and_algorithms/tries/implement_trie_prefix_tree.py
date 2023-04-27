# O(1) time | O(n) space

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root 
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode
            cur = cur.children 
        cur.endOfWord = True 
    
    def search(self, word: str) -> bool:
        cur = self.root 
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children
        return cur.endOfWord 
    
    def startWith(self, prefix: str) -> bool:
        cur = self.root 
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children
        return True
            