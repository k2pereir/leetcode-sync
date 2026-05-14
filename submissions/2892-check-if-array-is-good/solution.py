class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) == max(nums) + 1:
            ordered = sorted(nums)
            if len(nums) - 1 != len(set(ordered[:-1])):
                return False
            else:
                return True
        else:
            return False
