class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = dict(Counter(magazine))
        for char in ransomNote:
            if char in m and m[char] > 0:
                    m[char] -= 1
            else:
                return False
        return True
