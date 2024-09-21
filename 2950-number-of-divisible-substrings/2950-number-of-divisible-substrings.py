class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        dic={"a":1, "b":1, "c":2, "d":2, "e":2, "f":3, "g":3, "h":3, "i":4, "j":4, "k":4, "l":5, "m":5, "n":5, "o":6, "p":6, "q":6, "r":7, "s":7, "t":7, "u": 8, "v": 8, "w":8, "x":9, "y":9, "z":9}
        res=0
        for i in range(len(word)):
            running_count=0
            for j in range(i, len(word)): 
                running_count+=dic[word[j]]
                if running_count % len(word[i:j+1]) == 0:
                    res+=1
        return res
