class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # is a backtracking problem!
        results = []

        def backtrack(index, path):
            # base case:
            if index >= len(nums) or index < 0:
                results.append(path.copy())
                return

            # decision 1: include
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # decision 2: don't include
            backtrack(index + 1, path)

        backtrack(0, [])
        return results
