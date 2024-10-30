#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_sum = cur_sum = nums[0]
        s = start = 0
        end = 1

        for i in range(1, n):
            if cur_sum < 0:
                s = i
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]

            if cur_sum > max_sum:
                start = s
                end = i
                max_sum = cur_sum
        
        return nums[start:end+1]




        
# @lc code=end

