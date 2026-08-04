class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new[j][n - i - 1] = matrix[i][j]
        print("this is n")
        matrix[:] = new
