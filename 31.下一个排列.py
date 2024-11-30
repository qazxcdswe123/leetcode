#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        i = n - 2
        # find the first number that is smaller than it's right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                # find the first number that is bigger than nums[i]
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        reverse(nums, i + 1, n - 1)


# @lc code=end
