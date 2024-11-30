#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
"""

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        # A dictionary to map original nodes to their clones
        lookup = {}

        def dfs(curr_node):
            if curr_node in lookup:
                return lookup[curr_node]

            # Clone the current node
            clone = Node(curr_node.val)
            lookup[curr_node] = clone

            # Recursively clone all the neighbors
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


# @lc code=end
