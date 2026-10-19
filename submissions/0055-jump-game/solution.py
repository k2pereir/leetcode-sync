from functools import cache
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        target = len(nums) - 1
        
        @cache
        def check(curr):
            # base case: you've reached the end
            if curr >= target:
                return True
            for i in range(nums[curr], 0, -1): # biggest to smallest so we go faster
                if check(curr + i):
                    return True
            return False

        return check(0)

