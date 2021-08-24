# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
# 还有一个 random 指针指向链表中的任意节点或者 null。


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        d = {}  # 用一个hash map来保证字典的radom指向的是和原来的一样
        res = head
        # 复制各节点的值，建立一一对应关系
        while res:
            d[res] = Node(res.val)
            res = res.next
        # 构建新的节点的radom和next的指向
        res = head
        while res:
            d[res].next = d.get(res.next)
            d[res].random = d.get(res.random)
            res = res.next
        # 返回新的链表的头节点
        return d[head]

