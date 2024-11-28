class Node:

    def __init__(self, key, value, pre, next):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}  # key: node
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def top(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def get(self, key: int) -> int:
        node = self.data.get(key)
        if not node:
            return -1
        self.top(node)
        return node.value

    def delete(self):
        node = self.tail.pre
        del self.data[node.key]
        node.pre.next = self.tail
        self.tail.pre = node.pre

    def put(self, key: int, value: int) -> None:
        node = self.data.get(key)
        if node:
            self.top(node)
            node.value = value
        else:
            node = Node(key, value, self.head, self.head.next)
            self.head.next.pre = node
            self.head.next = node
            self.data[key] = node

            if len(self.data) > self.capacity:
                self.delete()

        # print(self.data)
        # node = self.head
        # while node:
        #     print(node, node.key, node.value)
        #     node = node.next


lru = LRUCache(2)
lru.put(1, 1)  # ; // 缓存是 {1=1}
lru.put(2, 2)  # ; // 缓存是 {1=1, 2=2}
print(lru.get(1))  # ;    // 返回 1
lru.put(3, 3)  # ; // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
print(lru.get(2))  # ;    // 返回 -1 (未找到)
lru.put(4, 4)  # ; // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
print(lru.get(1))  # ;    // 返回 -1 (未找到)
print(lru.get(3))  # ;    // 返回 3
print(lru.get(4))  # ;    // 返回 4
