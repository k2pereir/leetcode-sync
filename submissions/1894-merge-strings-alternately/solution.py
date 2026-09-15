class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        one = list(word1)
        two = list(word2)
        new = []
        shorter_length = min(len(one), len(two))
        for i in range(shorter_length):
            new.append(one[i])
            new.append(two[i])
        if len(one) > len(two):
            for i in range(len(two), len(one)):
                new.append(one[i])
        if len(two) > len(one):
            for i in range(len(one), len(two)):
                new.append(two[i])
        return "".join(new)
