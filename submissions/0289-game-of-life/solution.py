class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_live_neighbors(r, c):
            live = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                        live += board[nr][nc]
            return live

        dies = set()
        lives = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                live = get_live_neighbors(r, c)
                if board[r][c] == 1:
                    if live < 2 or live > 3:
                        dies.add((r, c))
                else:
                    if live == 3:
                        lives.add((r, c))

        for r, c in dies:
            board[r][c] = 0
        for r, c in lives:
            board[r][c] = 1
