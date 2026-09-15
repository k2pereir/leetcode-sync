class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # a row is valid if
        valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        columns = [[row[i] for row in board] for i in range(len(board[0]))]

        for i in range(len(board)):
            trimmed = [x for x in board[i] if x.isdigit()]
            if not set(trimmed).issubset(valid):
                return False
            if len(trimmed) != len(set(trimmed)):
                return False
            trimmed_col = [x for x in columns[i] if x.isdigit()]
            if not set(trimmed_col).issubset(valid):
                return False
            if len(trimmed_col) != len(set(trimmed_col)):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for x in range(3):
                    for y in range(3):
                        box.append(board[i + x][j + y])
        
                trimmed = [num for num in box if num.isdigit()]
                if len(trimmed) != len(set(trimmed)):
                    return False

        return True

