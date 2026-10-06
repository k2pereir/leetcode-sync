class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mods = [0] * len(nums)
        for i in range(len(nums)):
            mods[(i + k) % len(nums)] = nums[i]
        nums[:] = mods
