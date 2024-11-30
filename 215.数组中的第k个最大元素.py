#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(arr, left, right):
            pivot = arr[right]
            pi = left
            for i in range(left, right):
                if arr[i] < pivot:
                    arr[i], arr[pi] = arr[pi], arr[i]
                    pi += 1
            arr[pi], arr[right] = arr[right], arr[pi]
            return pi

        def select(arr, left, right, k):
            if left == right:
                return arr[left]

            pi = partition(arr, left, right)
            if pi == k:
                return arr[pi]
            elif pi > k:
                return select(arr, left, pi - 1, k)
            else:
                return select(arr, pi + 1, right, k)

        return select(nums, 0, len(nums) - 1, len(nums) - k)


# @lc code=end
