#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = n - 1
        top = 0
        bot = m - 1
        ret = []
        while left <= right and top <= bot:
            for c in range(left, right + 1):
                ret.append(matrix[top][c])
            for r in range(top + 1, bot + 1):
                ret.append(matrix[r][right])
            if top != bot and left != right:
                for c in range(right - 1, left, -1):
                    ret.append(matrix[bot][c])
                for r in range(bot, top, -1):
                    ret.append(matrix[r][left])
            left += 1
            right -= 1
            top += 1
            bot -= 1
        return ret
            

        
# @lc code=end

