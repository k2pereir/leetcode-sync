class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        unique = list(set(nums))
        unique.sort()

        maxx = 1
        current = 1

        for i in range(1, len(unique)):
            if unique[i] - unique[i - 1] == 1:
                current += 1
            else:
                maxx = max(maxx, current)
                current = 1
        
        return max(maxx, current)
