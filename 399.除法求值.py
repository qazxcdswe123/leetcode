#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#

# @lc code=start
class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1.0

            if y in graph[x]:
                return graph[x][y]

            visited.add(x)
            for n in graph[x]:
                if n not in visited:
                    val = dfs(n, y, visited)
                    if val != -1.0:
                        return val * graph[x][n]
            return -1.0

        ans = []
        for x, y in queries:
            ans.append(dfs(x, y, set()))

        return ans


# @lc code=end
