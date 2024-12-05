#
# @lc app=leetcode.cn id=2056 lang=python3
# @lcpr version=30204
#
# [2056] 棋盘上有效移动组合的数目
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def gen_moves(self, x0, y0, dirs):
        SIZE = 8
        moves = [(x0, y0, 0, 0, 0)]
        for dx, dy in dirs:
            x, y = x0 + dx, y0 + dy
            step = 1
            while 0 < x <= SIZE and 0 < y <= SIZE:
                moves.append((x0, y0, dx, dy, step))
                x += dx
                y += dy
                step += 1
        return moves

    def is_valid(self, move1, move2):
        x1, y1, dx1, dy1, step1 = move1
        x2, y2, dx2, dy2, step2 = move2
        for i in range(max(step1, step2)):
            if i < step1:
                x1 += dx1
                y1 += dy1
            if i < step2:
                x2 += dx2
                y2 += dy2
            if x1 == x2 and y1 == y2:
                return False
        return True

    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        rook_dirs = (-1, 0), (1, 0), (0, -1), (0, 1)  # 上下左右
        bishop_dirs = (1, 1), (-1, 1), (-1, -1), (1, -1)  # 斜向
        piece_dirs = {"r": rook_dirs, "b": bishop_dirs, "q": rook_dirs + bishop_dirs}
        all_moves = [
            self.gen_moves(x, y, piece_dirs[piece[0]])
            for piece, (x, y) in zip(pieces, positions)
        ]
        n = len(pieces)
        path = [None] * n
        ans = 0

        def dfs(i):
            if i == n:
                nonlocal ans
                ans += 1
                return
            for m in all_moves[i]:
                if all(self.is_valid(m, m2) for m2 in path[:i]):
                    path[i] = m
                    dfs(i + 1)

        dfs(0)
        return ans


# @lc code=end


#
# @lcpr case=start
# ["rook"]\n[[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# ["queen"]\n[[1,1]]\n
# @lcpr case=end

# @lcpr case=start
# ["bishop"]\n[[4,3]]\n
# @lcpr case=end

# @lcpr case=start
# ["rook","rook"]\n[[1,1],[8,8]]\n
# @lcpr case=end

# @lcpr case=start
# ["queen","bishop"]\n[[5,7],[3,4]]\n
# @lcpr case=end

#
