'''
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.endOfWord = False

    def insert(self, word: str) -> None:
        node = self
        
        for c in word:
            node = node.children[c]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.endOfWord
   

    def startsWith(self, prefix: str) -> bool:
        
        node = self
        
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
 