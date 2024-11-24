#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        diff = [prices[i] - prices[i - 1] for i in range(1, n)]
        return sum([d for d in diff if d > 0])
        
# @lc code=end

