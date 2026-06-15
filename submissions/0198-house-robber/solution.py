import heapq
class Solution:
    def rob(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for i in nums:
            temp = max(i + one, two) #either rob the house next to or the house over
            one = two
            two = temp
        return two
