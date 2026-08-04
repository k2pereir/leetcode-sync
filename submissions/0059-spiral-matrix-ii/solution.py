class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        output = [[0 for _ in range(n)] for _ in range(n)]

        left = 0
        right = n
        top = 0
        bottom = n

        curr = 1

        while left < right and top < bottom:
            for i in range(left, right):
                output[top][i] = curr
                curr += 1
            top += 1
            for i in range(top, bottom):
                output[i][right - 1] = curr
                curr += 1
            right -= 1

            if not(left < right and top < bottom):
                break

            for i in range(right - 1, left - 1, -1):
                output[bottom - 1][i] = curr
                curr += 1
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                output[i][left] = curr
                curr += 1
            left += 1
        return output
