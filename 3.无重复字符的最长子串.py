#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        left = 0
        ans = 0
        window = 0
        for c in s:
            while c in lookup:
                lookup.remove(s[left])
                left += 1
                window -= 1
            lookup.add(c)
            window += 1
            ans = max(ans, len(lookup))
        
        return ans



        
# @lc code=end

