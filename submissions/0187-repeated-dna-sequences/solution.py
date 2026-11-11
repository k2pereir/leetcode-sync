class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        substrings = []
        if len(s) < 10:
            return substrings
        left = 0
        right = 10
        for i in range(len(s) - 10 + 1):
            substrings.append(s[i:i + 10])
        duplicates = [dupe for dupe, count in Counter(substrings).items() if count > 1]
        return duplicates


