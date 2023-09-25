class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open_close={')':'(', '}':'{', ']':'['}
        for char in s:
            if char == '(' or char == '{' or char=='[':
                stack.append(char)
            if char == ')' or char == '}' or char==']':
                if len(stack) == 0: 
                    return False
                if len(stack) >= 1 and open_close[char] == stack[-1]:
                    stack.pop()
                elif len(stack)>=1 and open_close[char] not in stack:
                    return False
        return len(stack) == 0 

        