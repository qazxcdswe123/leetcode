#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)
        ans = 0
        sum = 0
        while right < n:
            sum += nums[right]
            while sum >= target:
                ans = right - left + 1 if ans == 0 else min(ans, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1
        return ans
        
# @lc code=end

