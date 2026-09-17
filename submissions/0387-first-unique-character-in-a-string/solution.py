class Solution:
    def firstUniqChar(self, s: str) -> int:
        # get all the occurances
        chars = {}
        for char in s:
            if chars.get(char):
                chars[char] += 1
            else:
                chars.update({char: 1})
        
        # find the first 1 and get its index
        for key, value in chars.items():
            if value == 1:
                return list(s).index(key)
        return -1
