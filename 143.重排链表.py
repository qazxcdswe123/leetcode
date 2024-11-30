#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        
        def mid(head):
            if not head or not head.next:
                return head

            slow = head
            fast = head.next
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(l1, l2):
            while l1 and l2:
                t1, t2 = l1.next, l2.next
                l1.next = l2
                l1 = t1
                l2.next = l1
                l2 = t2
        
        if not head or not head.next:
            return head
        
        mid_node = mid(head)
        l1 = head
        l2 = mid_node.next
        mid_node.next = None
        l2 = reverse(l2)
        merge(l1, l2)
        
        
# @lc code=end

