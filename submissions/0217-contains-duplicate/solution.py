class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # curr = 10000
        # for i in range(len(nums)):
        #     if nums[i] == curr:
        #         return True
        #     curr = nums[i]
        # return False

        # ^^ that was a naive approach
        # but we could also just be clever and go!
        new = set(nums)
        if len(new) != len(nums):
            return True
        return False
