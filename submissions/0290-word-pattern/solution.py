class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = {}
        chars = {}
        patt = list(pattern)

        if len(s.split()) != len(patt):
            return False
        for w, c in zip(s.split(), patt):
            if w in words and words[w] != c or c in chars and chars[c] != w:
                return False
            words[w] = c
            chars[c] = w
        return True
