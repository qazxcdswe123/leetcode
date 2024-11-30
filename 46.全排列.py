#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def bt(end):
            if end == n:
                ans.append(nums[:])
                return

            for i in range(end, n):
                nums[i], nums[end] = nums[end], nums[i]
                bt(end + 1)
                nums[i], nums[end] = nums[end], nums[i]

        bt(0)
        return ans


# @lc code=end
