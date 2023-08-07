class TrieNode: 
    #note: thought to create children, but opted against it (mistake!!!)
    def __init__(self):
        self.children={}
        self.end=None
        
class Trie:

    def __init__(self):
        #hashmap to store the children of the node 
        #root node is going to be empty and the letters of the alphabet are going to    be descendents 
        self.head=TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr = curr.children[char]
        curr.end = True
            
    def search(self, word: str) -> bool:
        curr=self.head
        for char in word: 
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.head
        for char in prefix:
            if char not in curr.children: 
                return False
            curr = curr.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)