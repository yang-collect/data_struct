# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        target = l3 = ListNode()  # 初始化目标链表以及中间链表
        carry, value = 0, 0  # 初始化进位以及当前节点value值
        while l1 or l2 or carry:  # 当l1、l2走完且当前进位为0时，停止遍历
            value = carry  # 当前value为进位
            if l1:  # 当l1不是空指针时，将l1.val加在value上，遍历下一个节点
                value += l1.val
                l1 = l1.next

            if l2:  # 同上理
                value += l2.val
                l2 = l2.next
            # 当前value可能为一个两位数，故需要将其十位数作为carry进位，个位数作为value
            carry, value = divmod(value, 10)
            # 将l3的next节点指向value对应的一个实例化节点
            l3.next = ListNode(value)
            # 继续遍历
            l3 = l3.next

        return target.next
