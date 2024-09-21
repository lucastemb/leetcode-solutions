class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #count character for each
        #create hash for each combo of characters
        anagram = {}
        i=0
        res=[]
        for string in strs:
            letters = [0]*26
            #create hash
            for letter in string:
                letters[ord('a')-ord(letter)]+=1
            #add hash 
            if tuple(letters) not in anagram:
                anagram[tuple(letters)] = i
                templist = []
                templist.append(string)
                res.append(templist)
                i+=1
            else:
                index = anagram[tuple(letters)]
                res[index].append(string)
        return res


            