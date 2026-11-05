class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for val1 in arr1:
            for val2 in arr2:
                if abs(val1 - val2) <= d:
                    break
            else:
                count += 1
        return count
