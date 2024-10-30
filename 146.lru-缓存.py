#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#

# @lc code=start
class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.head.next = self.head
        self.head.prev = self.head

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_front(self, node: ListNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.add_front(node)
        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.add_front(node)

            if len(self.cache) > self.capacity:
                node = self.head.prev
                self.remove(node)
                self.cache.pop(node.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
