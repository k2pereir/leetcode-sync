class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # requires backtracking 
        combos = list()
        # what does index here represent??
        def backtrack(index, path, remaining):
            # base case, you've reached the target
            if remaining == 0:
                combos.append(path.copy())
                return

            if remaining < 0 or index >= len(candidates):
                return

            # use this letter again
            path.append(candidates[index])
            backtrack(index, path, remaining - candidates[index])
            path.pop()

            # or skip it
            backtrack(index + 1, path, remaining)
        
        backtrack(0, [], target)
        return combos

