#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs_mark_safe(x, y):
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != "O":
                return
            board[x][y] = "A"
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs_mark_safe(x + dx, y + dy)

        for i in range(m):
            for j in range(n):
                is_edge = i == 0 or j == 0 or i == m - 1 or j == n - 1
                if is_edge and board[i][j] == "O":
                    dfs_mark_safe(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"


# @lc code=end
