class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1:
            return mat[0]
        
        row = len(mat)
        column = len(mat[0])

        output = [[] for _ in range(row + column - 1)]

        for i in range(row):
            for j in range(column):
                if (i + j) % 2 == 0:
                    output[i + j].insert(0, mat[i][j])
                else:
                    output[i + j].append(mat[i][j])
        
        return [item for sublist in output for item in sublist]
