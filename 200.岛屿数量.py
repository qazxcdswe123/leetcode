# #
# # @lc app=leetcode.cn id=200 lang=python3
# #
# # [200] 岛屿数量
# #

# # @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()

        def dfs(i, j):
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[0])
                or (i, j) in seen
                or grid[i][j] == "0"
            ):
                return
            seen.add((i, j))
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(i + x, j + y)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in seen:
                    count += 1
                    dfs(i, j)
        return count


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         def dfs(i, j):
#             if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
#                 return
#             # set '1' to '0'
#             grid[i][j] = '0'
#             for x, y in directions:
#                 dfs(i + x, j + y)
#         count = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     count += 1
#                     dfs(i, j)
#         return count


# # @lc code=end
