class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars={}
        l=0
        maxCount=0
        for r in range(len(s)): 
            chars[s[r]] = 1 + chars.get(s[r],0)
            maxCount=max(maxCount, chars[s[r]])
            
            if (r-l)+1-maxCount > k:
                chars[s[l]]-=1
                l+=1
            
        return (r-l)+1
            
            
            