class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        triplets = []
        inArr=set()
        s = sorted(arr)
        for i in range(len(arr)):
            l=i+1
            r=len(s)-1
            while l < r:
                if s[l] + s[r] < abs(s[i]):
                    l+=1
                elif s[l] + s[r] > abs(s[i]):
                    r-=1
                else:
                    if ((s[i], s[l], s[r])) not in inArr:
                        triplets.append([s[i], s[l], s[r]])
                        inArr.add((s[i], s[l], s[r]))
                    l+=1
        return triplets
        