class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = []
        cols = []

        # record all the zeroes
        for r, row in enumerate(matrix):
            for c, value in enumerate(row):
                if value == 0:
                    rows.append(r)
                    cols.append(c)

        # make the in place change
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rows or c in cols:
                    matrix[r][c] = 0
