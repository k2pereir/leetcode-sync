class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = list(s)
        prev = None 
        buffer = None
        int = 0
        for i in range(len(s)): 
            buffer = s[i]
            if buffer == "V" and prev == "I": 
                int = int + 4 - 1
            elif buffer == "X" and prev == "I":
                int = int + 9 - 1
            elif buffer == "L" and prev == "X":
                int = int + 40 - 10
            elif buffer == "C" and prev == "X":
                int = int + 90 - 10 
            elif buffer == "D" and prev == "C": 
                int = int + 400 - 100
            elif buffer == "M" and prev == "C":
                int = int + 900 - 100
            else: 
                int = int + romans.get(s[i])
            prev = s[i]
        return int

