#
# @lc app=leetcode.cn id=3001 lang=python3
# @lcpr version=30204
#
# [3001] 捕获黑皇后需要的最少移动次数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minMovesToCaptureTheQueen(
        self, a: int, b: int, c: int, d: int, e: int, f: int
    ) -> int:
        # 车与皇后处在同一行，且中间没有象
        if a == e and (c != a or d <= min(b, f) or d >= max(b, f)):
            return 1
        # 车与皇后处在同一列，且中间没有象
        if b == f and (d != b or c <= min(a, e) or c >= max(a, e)):
            return 1
        # 象、皇后处在同一条对角线，且中间没有车
        if abs(c - e) == abs(d - f) and (
            (c - e) * (b - f) != (a - e) * (d - f) or a < min(c, e) or a > max(c, e)
        ):
            return 1
        return 2


# @lc code=end


#
# @lcpr case=start
# 1\n1\n8\n8\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 5\n3\n3\n4\n5\n2\n
# @lcpr case=end

#
