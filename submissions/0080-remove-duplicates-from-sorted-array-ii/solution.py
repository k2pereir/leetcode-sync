class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = {}
        cutoff = 0
        for num in nums:
            count = seen.get(num, 0)
            if count < 2:
                seen[num] = count + 1
                nums[cutoff] = num
                cutoff += 1
        nums[:] = nums[:cutoff]
        return cutoff
