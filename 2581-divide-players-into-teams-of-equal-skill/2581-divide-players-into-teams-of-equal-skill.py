class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        res=[]
        s=0
        stack=[]
        target=(skill[0]+skill[len(skill)-1])
        for i in range(len(skill)//2):
            res.append((skill[i], skill[len(skill)-1-i]))
        
        for weak, strong in res:
            if weak + strong != target: 
                return -1
            s+=weak*strong
        return s
            

            