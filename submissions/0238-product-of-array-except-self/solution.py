class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time meaning i can only go through all elements in the list once
        # can't divide so can't multiply everything and divide by the number

        left = [1] * len(nums)
        right = [1] * len(nums)
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        
        return result




