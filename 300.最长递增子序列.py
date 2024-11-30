#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for n in nums:
            if not arr or arr[-1] < n:
                arr.append(n)
            else:
                idx = bisect.bisect_left(arr, n)
                arr[idx] = n
        return len(arr)


# @lc code=end
