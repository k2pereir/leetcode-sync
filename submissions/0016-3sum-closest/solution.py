class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        best_sum = None
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < diff:
                    best_sum = sum
                    diff =abs(sum - target)
                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
        return best_sum
