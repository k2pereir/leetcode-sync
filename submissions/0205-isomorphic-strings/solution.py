class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        td = {}

        for c1, c2 in zip(s, t):
            if (c1 in sd and sd[c1] != c2) or (c2 in td and td[c2] != c1):
                return False
            sd[c1] = c2
            td[c2] = c1
        return True



