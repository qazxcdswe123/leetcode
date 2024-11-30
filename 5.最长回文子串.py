#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(L, R):
            while L >= 0 and R < n and s[L] == s[R]:
                L -= 1
                R += 1
            return L + 1, R - 1

        start, end = 0, 0
        for i in range(n):
            L1, R1 = expand(i, i)
            L2, R2 = expand(i, i + 1)
            if R1 - L1 > end - start:
                start, end = L1, R1
            if R2 - L2 > end - start:
                start, end = L2, R2
        return s[start : end + 1]


# @lc code=end
