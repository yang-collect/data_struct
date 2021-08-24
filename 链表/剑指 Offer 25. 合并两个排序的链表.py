# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
# 示例1：

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        target = l3 = ListNode()  # 初始化目标链表
        while l1 and l2:
            # 当两个链表都不为空时，比较当前指针值的大小，将其中较大者放入l3的后面
            if l1.val >= l2.val:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            else:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            l3 = l3.next
        l3.next = l1 if l1 else l2  # 将其中非空的部分添加在l3尾部
        return target.next
