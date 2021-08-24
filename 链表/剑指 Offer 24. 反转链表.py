# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

#  

# 示例:

# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None  # 初始化逆序链表
        cur = head
        while cur:
            # 交换链表前后值的顺序，并访问下一个节点
            cur.next, pre, cur = pre, cur, cur.next
        return pre
