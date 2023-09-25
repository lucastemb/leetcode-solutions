class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_close={')':'(', '}':'{', ']':'['}
        for c in s:
            if c not in open_close: 
                stack.append(c)
                continue
            if len(stack) == 0 or stack[-1]!=open_close[c]:
                return False
            stack.pop()
        return len(stack) == 0 

        