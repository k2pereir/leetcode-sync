class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        chars = Counter(t)
        req = len(set(t))
        window = defaultdict(int)
        sub = 0
        left = 0
        right = 0
        mw = float('inf'), None, None

        while right < len(s):
            char = s[right]
            window[char] += 1
            if char in chars and window[char] == chars[char]:
                sub += 1
            while left <= right and sub == req:
                char = s[left]
                if right - left + 1 < mw[0]:
                    mw = (right - left + 1, left, right)
                window[char] -= 1
                if char in chars and window[char] < chars[char]:
                    sub -= 1
                left += 1
            right += 1
        
        if mw[0] == float('inf'):
            return ""
        return s[mw[1]:mw[2] + 1]



        
