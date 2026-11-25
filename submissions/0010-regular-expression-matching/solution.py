class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        grid = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        grid[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == "*":
                grid[0][i] = grid[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    grid[i][j] = grid[i - 1][j - 1]
                elif p[j - 1] == "*":
                    prev = p[j - 2]
                    # should we use prev 0 or more times
                    zero = grid[i][j - 2]
                    more = (prev == s[i - 1] or prev == ".") and grid[i - 1][j]
                    grid[i][j] = zero or more

        return grid[len(s)][len(p)]
