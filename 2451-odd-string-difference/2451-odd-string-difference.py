class Solution:
    def oddString(self, words: List[str]) -> str:
        count={}
        indexes={}
        for i in range(len(words)):
            char_arr=[]
            for j in range(1, len(words[i])):
                char_arr.append(ord(words[i][j])-ord(words[i][j-1]))
            count[tuple(char_arr)]=count.get(tuple(char_arr), 0)+1
            indexes[tuple(char_arr)]=i
        final = sorted(count.items(), key=lambda x: x[1])
        return words[indexes[final[0][0]]]

            

