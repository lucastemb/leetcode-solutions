class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        pairings=[]
        res=0
        for i in range(len(skill)//2):
            if i > 0 and skill[i]+skill[len(skill)-1-i] != sum(pairings[0]):
                return -1
            pairings.append((skill[i],skill[len(skill)-1-i])) 
            res+=(skill[i]*skill[len(skill)-1-i])
            
        return res
            