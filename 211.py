'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
    - WordDictionary() Initializes the object.
    - void addWord(word) Adds word to the data structure, it can be matched later.
    - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()
        
    def addWord(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):

            cur = root

            for i in range(j,len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.endOfWord
        
        return dfs(0, self.root)
        
