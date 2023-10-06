class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        target=(skill[0]+skill[len(skill)-1])
        res=0
        for i in range(len(skill)//2):
            if skill[i]+skill[len(skill)-1-i] != target:
                return -1
            res+=(skill[i]*skill[len(skill)-1-i])   
        return res

        #time: O(n*log(n))
        #space: O(1)

            