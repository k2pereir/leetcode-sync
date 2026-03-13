class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        length = 0
        substring = ""
        while right < len(s):
            substring += s[right]
            while len(substring) != len(set(substring)):
                substring = substring[1:]
                left += 1
            length = max(length, len(substring))
            right += 1

        return length

            
