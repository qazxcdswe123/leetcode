#
# @lc app=leetcode.cn id=67 lang=python3
# @lcpr version=30204
#
# [67] 二进制求和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na, nb = len(a), len(b)
        n = max(na, nb)
        res = []
        carry = 0
        for i in range(n):
            if i < na:
                carry += int(a[na - i - 1])
            if i < nb:
                carry += int(b[nb - i - 1])
            res.append(str(carry % 2))
            carry //= 2
        if carry:
            res.append("1")
        return "".join(res[::-1])


# @lc code=end


#
# @lcpr case=start
# "11"\n"1"\n
# @lcpr case=end

# @lcpr case=start
# "1010"\n"1011"\n
# @lcpr case=end

#
