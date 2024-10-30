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

            l, r = i + 1, n - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s == 0:
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1

        return ans


# @lc code=end
