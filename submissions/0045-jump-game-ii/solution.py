class Solution:
    def jump(self, nums: list[int]) -> int:
        target = len(nums) - 1
            
        @cache
        def check(curr):
            if curr >= target:
                return 0
            if nums[curr] == 0:
                return math.inf
            min_jumps = math.inf
            for i in range(1, nums[curr] + 1):
                min_jumps = min(min_jumps, 1 + check(curr + i))
            return min_jumps
        return check(0)
