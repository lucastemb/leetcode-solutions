class Solution:
    def oddString(self, words: List[str]) -> str:
        diff={}
        ans={}
        for word in words:
            res=[]
            for i in range(1, len(word)):
                res.append(ord(word[i])-ord(word[i-1]))
            diff[tuple(res)]=diff.get(tuple(res),0)+1
            ans[tuple(res)]=word
        print(min(diff.items(), key= lambda x: x[1]))
        least_freq_word=min(diff.items(), key= lambda x: x[1])[0]
        return ans[least_freq_word]
