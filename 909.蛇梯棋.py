#
# @lc app=leetcode.cn id=909 lang=python3
#
# [909] 蛇梯棋
#

# @lc code=start
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dp = [-1] * (n * n + 1)
        dp[1] = 0
        q = deque([1])

        def get(v):
            x, y = divmod(v - 1, n)
            if x % 2 == 0:
                return n - 1 - x, y
            return n - 1 - x, n - 1 - y

        while q:
            u = q.popleft()
            if u == n * n:
                return dp[u]
            for i in range(1, 7):
                v = u + i
                if v > n * n:
                    break
                x, y = get(v)
                if board[x][y] != -1:
                    v = board[x][y]
                if dp[v] == -1:
                    dp[v] = dp[u] + 1
                    q.append(v)

        return -1


# @lc code=end
