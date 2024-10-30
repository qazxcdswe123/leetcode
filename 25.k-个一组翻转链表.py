#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, tail):
        pre = tail.next
        p = head
        while pre != tail:
            nex = p.next
            p.next = pre
            pre = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pre = dummy
        while head:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return dummy.next


# @lc code=end
