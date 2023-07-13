class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window={}
        t_map={}
        res_len=float("infinity")
        res=[-1,-1]
        l=0
        have=0

        
        if t=="":
            return ""

        #traverse through list to get values of letters 
        for letter in t:
            t_map[letter]=1+t_map.get(letter,0)
        need=len(t_map)
        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)
            if s[r] in t_map and window[s[r]] == t_map[s[r]]:
                have+=1
            while have == need: 
                if ((r-l)+1) < res_len:
                    res=[l,r]
                    res_len=((r-l)+1)
                window[s[l]]-=1
                if s[l] in t_map and window[s[l]] < t_map[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l : r + 1] if res_len != float("infinity") else ""

                

            
