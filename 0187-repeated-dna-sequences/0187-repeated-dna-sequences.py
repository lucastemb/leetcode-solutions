class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences={}
        res=[]
        for i in range(len(s)-9):
            print(i)
            if s[i:i+10] in sequences and s[i:i+10] not in res: 
                res.append(s[i:i+10])
            sequences[s[i:i+10]]=1+sequences.get(s[i:i+10], 0)
        return res
            
            
        