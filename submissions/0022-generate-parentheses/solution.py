class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking problem!! 
        results = list()

        def backtrack(forwards, backwards, path):
            # base case:
            if forwards == 0 and backwards == 0:
                results.append("".join(path))
                return

            # decision 1: use a forwards
            if forwards > 0:
                path.append('(')
                backtrack(forwards - 1, backwards, path)
                path.pop()

            # decision 2: use a backwards
            if backwards > forwards:
                path.append(')')
                backtrack(forwards, backwards - 1, path)
                path.pop()
        
        backtrack(n, n, [])
        return results
