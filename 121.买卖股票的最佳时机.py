#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for p in prices:
            min_price = min(min_price, p)
            profit = max(profit, p - min_price)
        return profit

        
# @lc code=end

