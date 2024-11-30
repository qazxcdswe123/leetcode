#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        y, z = nums[-2], nums[-1]
        for i in range(n - 2):
            a = nums[i]

            if a + nums[i + 1] + nums[i + 2] > 0:
                break
            if a + y + z < 0:
                continue
            if i > 0 and a == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            while left < right:
                b, c = nums[left], nums[right]
                s = a + b + c
                if s == 0:
                    ans.append([a, b, c])
                    while left < right and b == nums[left]:
                        left += 1
                    while left < right and c == nums[right]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return ans
