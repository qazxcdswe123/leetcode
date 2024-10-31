#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # def partition(nums, left, right):
        #     pivot = nums[left]
        #     while left < right:
        #         while left < right and nums[right] >= pivot:
        #             right -= 1
        #         nums[left] = nums[right]
        #         while left < right and nums[left] <= pivot:
        #             left += 1
        #         nums[right] = nums[left]
        #     nums[left] = pivot
        #     return left

        # def qs(nums, left, rigth):
        #     if left < rigth:
        #         mid = partition(nums, left, rigth)
        #         qs(nums, left, mid-1)
        #         qs(nums, mid+1, rigth)

        # qs(nums, 0, len(nums)-1)
        # return nums
        
        # def merge_sort(nums):
        #     if len(nums) <= 1:
        #         return nums
        #     mid = len(nums) // 2
        #     left = merge_sort(nums[:mid])
        #     right = merge_sort(nums[mid:])
        #     return merge(left, right)

        # def merge(left, right):
        #     res = []
        #     i = j = 0
        #     while i < len(left) and j < len(right):
        #         if left[i] < right[j]:
        #             res.append(left[i])
        #             i += 1
        #         else:
        #             res.append(right[j])
        #             j += 1
        #     res += left[i:]
        #     res += right[j:]
        #     return res

        # return merge_sort(nums)

        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
            
        def heap_sort(arr):
            n = len(arr)
            for i in range(n // 2 - 1, -1, -1):
                heapify(arr, n, i)
            for i in range(n - 1, 0, -1):
                arr[i], arr[0] = arr[0], arr[i]
                heapify(arr, i, 0)
            return arr

        return heap_sort(nums)
