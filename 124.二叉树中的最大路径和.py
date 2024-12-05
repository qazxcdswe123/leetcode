#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node):
            if not node:
                return 0
            
            L = max(0, dfs(node.left))
            R = max(0, dfs(node.right))
            s = node.val + L + R
            nonlocal ans
            ans = max(ans, s)
            return node.val + max(L, R)
        dfs(root)
        return ans




        
# @lc code=end

