class Solution:
    def isHappy(self, n: int) -> bool:
        computed=set()
        if n == 1:
            return True
        while n != 1 and n not in computed: 
            computed.add(n)
            final_sum=0
            while n > 0: 
                final_sum+=(n%10)**2
                n=n//10
            n=final_sum
            if n == 1:
                return True
        return False
        