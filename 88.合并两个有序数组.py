#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = m + n - 1
        while m > 0 and n > 0:
            a, b = nums1[m - 1] , nums2[n - 1]
            if a > b:
                nums1[idx] = a
                m -= 1
            else:
                nums1[idx] = b
                n -= 1
            idx -= 1

        while m > 0:
            nums1[idx] = nums1[m - 1]
            idx -= 1
            m -= 1
        
        while n > 0:
            nums1[idx] = nums2[n - 1]
            idx -= 1
            n -= 1
        
# @lc code=end

