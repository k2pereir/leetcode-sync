class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        # otherwise find the greatest common denominator of the lengths 
        import math
        gcd = math.gcd(len(str1), len(str2))
        mush = str1 + str2
        return mush[:gcd]
