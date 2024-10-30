#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                continue
            else:
                res.append(
                    str(start) + "->" + str(nums[i - 1])
                    if start != nums[i - 1]
                    else str(start)
                )
                start = nums[i]
            
        res.append(
            str(start) + "->" + str(nums[-1])
            if start != nums[-1]
            else str(start)
        )
        return res


# @lc code=end
