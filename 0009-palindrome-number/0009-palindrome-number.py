class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        s=""
        for letter in reversed(x):
            s+=letter
        return True if s == x else False
            
        
        