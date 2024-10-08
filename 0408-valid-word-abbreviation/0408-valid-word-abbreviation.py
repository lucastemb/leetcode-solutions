class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if word == abbr: 
            return True
        i,j=0,0
        count = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isnumeric(): 
                if abbr[j] == '0':
                    return False
                count = 0 
                while j < len(abbr) and abbr[j].isnumeric():
                    count = count * 10 + int(abbr[j])
                    j+=1
                i+=count
            else:
                if i >= len(word)-1 and word[i] != abbr[j]:
                    return False
                i+=1
                j+=1
        return i == len(word) and j == len(abbr)




        