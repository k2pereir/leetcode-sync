class Solution:
    def myPow(self, x: float, n: int) -> float:
        # # base case is when n = 1
        # if n == 1: 
        #     return x 
        
        # if n > 0: 
        #     return x * self.myPow(x, n - 1)
        # else: 
        #     n = n * -1
        #     return 1/(x * self.myPow(x, n - 1))
        import math 
        return math.pow(x, n)
