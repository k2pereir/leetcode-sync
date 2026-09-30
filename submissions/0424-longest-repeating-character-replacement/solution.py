class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        count = {}
        slow = 0
        maxfreq = 0
        maxlength = 0
        for fast in range(len(s)):
            count[s[fast]] = count.get(s[fast], 0) + 1
            maxfreq = max(maxfreq, count[s[fast]])
            while (fast - slow + 1) - maxfreq > k:
                count[s[slow]] -= 1
                slow += 1
            maxlength = max(maxlength, fast - slow + 1)
        return max(maxlength, fast - slow + 1)
