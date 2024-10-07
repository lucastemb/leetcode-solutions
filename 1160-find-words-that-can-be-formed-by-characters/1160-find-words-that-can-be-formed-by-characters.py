class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        letters = {}
        for letter in chars: 
            letters[letter] = letters.get(letter, 0)+1
        #create hashmap of all letters
        res=0
        #create a hashmap that stores all of the characters
        for word in words: 
            freq={} 
            #
            for c in word: 
                freq[c] = freq.get(c, 0)+1
            for x,y in freq.items():
                if (x in letters and y > letters[x]) or x not in letters:
                    break
            else:
                res+=len(word)
        return res
        
        


        