#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        last_sorted = head
        cur = head.next
        while cur:
            if last_sorted.val <= cur.val:
                last_sorted = last_sorted.next
            else:
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next
                last_sorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
            cur = last_sorted.next
        return dummy.next
        
# @lc code=end

