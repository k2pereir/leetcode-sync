class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = {}
        for num in nums:
            if counts.get(num):
                counts[num] += 1
            else:
                counts[num] = 1
        return max(counts, key=counts.get)
