class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dupes = [i for i, count in Counter(nums).items() if count > 1]
        for i in range(len(nums)):
            if nums[i] in dupes:
                indices = [j for j, val in enumerate(nums) if val == nums[i]]
                for j in indices:
                    if i != j:
                        if abs(i - j) <= k:
                            return True
        return False
