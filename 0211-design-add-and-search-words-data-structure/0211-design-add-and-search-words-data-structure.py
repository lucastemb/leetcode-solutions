#implement Trie data structure 
class Node: 
    def __init__(self):
        self.children={}
        self.end=False
class WordDictionary:
    def __init__(self):
        self.head = Node()
    def addWord(self, word: str) -> None:
        curr = self.head
        for i in range(len(word)):
            if word[i] not in curr.children:
                curr.children[word[i]]=Node()
            curr=curr.children[word[i]]
        curr.end = True


    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c=word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False 
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.end
        return dfs(0, self.head)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)