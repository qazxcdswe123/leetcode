#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        builder = []

        def bt(left_paren_cnt, total_cnt):
            if total_cnt == n * 2:
                ans.append("".join(builder))
                return
            if left_paren_cnt < n:
                builder.append("(")
                bt(left_paren_cnt + 1, total_cnt + 1)
                builder.pop()
            if left_paren_cnt * 2 > total_cnt:
                builder.append(")")
                bt(left_paren_cnt, total_cnt + 1)
                builder.pop()
        
        bt(0, 0)
        return ans


# @lc code=end
