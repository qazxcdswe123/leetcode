#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left_list, right_list):
            dummy = ListNode()
            cur = dummy
            while left_list and right_list:
                if left_list.val < right_list.val:
                    cur.next = left_list
                    left_list = left_list.next
                else:
                    cur.next = right_list
                    right_list = right_list.next
                cur = cur.next
            if left_list:
                cur.next = left_list
            if right_list:
                cur.next = right_list
            return dummy.next

        def merge_sort(head):
            if not head or not head.next:
                return head
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            left, right = head, mid
            left = merge_sort(left)
            right = merge_sort(right)
            return merge(left, right)
        return merge_sort(head)


# @lc code=end
