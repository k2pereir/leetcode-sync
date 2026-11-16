class Solution:
    def isHappy(self, n: int) -> bool:
        seen = dict()
        seen[n] = 1
        while n != 1:
            s = 0
            for digit in str(n):
                s += int(digit) ** 2
            n = s
            if n in seen:
                return False
            seen[n] = 1
        return True
            



