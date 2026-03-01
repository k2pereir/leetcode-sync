class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # what am i doing in my head? when solving? putting into rows, reading the rows
        # probably not an optimal solution but lets get something down
        lists = list()
        final = list()
        count = 0
        direction = 1
        if numRows == 1:
            return s
        for i in range(numRows):
            lists.append(list())
        for i in range(len(s)):
            lists[count].append(s[i])
            if count == 0:
                direction = 1
            if count == numRows - 1:
                direction = -1
            count += direction
        for i in range(numRows):
            for j in range(len(lists[i])):
                final.append(lists[i][j])
        return ''.join(final)
