class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # recursion isn't really gonna work because it'll definitely exceed time constraints since you have to keep rebuilding
        # so the optimal solution is to use hash maps
        prefixes = {0: 1} #bc we've seen the sum of 0 once already
        total = 0
        curr = 0

        for num in nums:
            curr += num
            if curr - k in prefixes:
                total += prefixes[curr - k]
            prefixes[curr] = prefixes.get(curr, 0) + 1
            
        return total
