#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        edges = defaultdict(list)
        indeg = [0] * numCourses

        for to_study, need in prerequisites:
            edges[need].append(to_study)
            indeg[to_study] += 1

        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        while q:
            u = q.popleft()
            ans.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return ans if len(ans) == numCourses else []


# @lc code=end
