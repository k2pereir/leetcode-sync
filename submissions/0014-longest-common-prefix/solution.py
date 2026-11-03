class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        first = strs[0]
        for i in range(len(first)):
            prefix += first[i]
            for word in strs[1:]:
                if i >= len(word) or word[0:i+1] != prefix:
                    return prefix[:-1]
        return prefix
