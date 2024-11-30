#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stk = []
        for i, h in enumerate(height):
            while stk and h >= height[stk[-1]]:
                bot_h = height[stk.pop()]
                if not stk:
                    break
                left = stk[-1]
                left_h = height[left]
                dh = min(left_h, h) - bot_h
                ans += (i - left - 1) * dh
            stk.append(i)
        return ans


# @lc code=end
