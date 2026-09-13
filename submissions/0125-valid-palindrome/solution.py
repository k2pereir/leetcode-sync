class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean it up so that everything is lowercase and a letter
        chars = "".join(filter(str.isalnum, s))
        chars = chars.lower()

        start = 0
        end = len(chars) - 1

        while start < end:
            if chars[start] != chars[end]:
                return False
            start = start + 1
            end = end - 1
        return True
        
