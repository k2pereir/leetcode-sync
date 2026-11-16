class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ranges = []
        prev = nums[0]
        start = nums[0]
        end = None
        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                if end is not None:
                    ranges.append(f"{start}->{end}")
                else:
                    ranges.append(str(start))
                start = nums[i]
                end = None
            else:
                end = nums[i]
            prev = nums[i]
        if end is not None:
            ranges.append(f"{start}->{end}")
        else:
            ranges.append(str(start))
        return ranges

