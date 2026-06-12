class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ""

        def find(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        for i in range(len(s)):
            s1 = find(i, i)
            s2 = find(i, i + 1)

            if len(s1) > len(substring):
                substring = s1

            if len(s2) > len(substring):
                substring = s2

        return substring
