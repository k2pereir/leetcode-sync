class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = dict() 
        for char in s: 
            if chars.get(char) is None: 
                chars.update({char: 1})
            else: 
                chars[char] = chars.get(char) + 1        
        for key in chars: 
            if chars.get(key) == 1:
                return s.index(key)
        return -1
