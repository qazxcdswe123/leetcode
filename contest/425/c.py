import heapq
import math
from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = [-num for num in nums]
        heapq.heapify(n)

        # x < 2k: op2
        # 2k < x < 2k + 1: both
        # x >= 2k+2: op1
        def doop1(x):
            return math.ceil(x / 2)

        def doop2(x):
            return x - k

        while op1 or op2:
            max_val = -heapq.heappop(n)
            if op1 and max_val >= 2 * k + 2:
                heapq.heappush(n, -doop1(max_val))
                op1 -= 1
                continue
            if op1 and 2 * k < max_val < 2 * k + 2:
                heapq.heappush(n, -doop1(max_val))
                op1 -= 1
                continue
            if op2 and k <= max_val <= 2 * k:
                heapq.heappush(n, -doop2(max_val))
                op2 -= 1
                continue
            break
        return -sum(n)
