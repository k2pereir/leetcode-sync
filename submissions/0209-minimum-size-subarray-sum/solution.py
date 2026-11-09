class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minl = float('inf')
        slow = 0
        curr = 0
        for fast in range(len(nums)):
            curr += nums[fast]
            while curr >= target:
                minl = min(minl, fast - slow + 1)
                curr -= nums[slow]
                slow += 1
        if minl == float('inf'):
            return 0
        return minl
                
