class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        temp=''
        for letter in s:
            if letter != ' ':
                temp+=letter
            else:
                if temp != '':
                    res.insert(0,temp)
                temp=''
        if temp != '':
                res.insert(0,temp)
        return ' '.join(res)
        