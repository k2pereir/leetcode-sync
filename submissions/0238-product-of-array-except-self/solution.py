class Solution:
    import math
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prods = []
        total = math.prod(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                prods.append(total // nums[i])
            else:
                prods.append(math.prod(nums[:i] + nums[i+1:]))
        return prods
