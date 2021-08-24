# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []  # 边界条件
        res, l = [], collections.deque([root])  # 初始化一个结果列表和一个待访问队列
        while l:
            # popleft弹出的是栈底的元素，这是因为访问的顺序是从左到右
            node = l.popleft()
            res.append(node.val)
            # 若左子节点存在，将左子节点加入待访问队列中
            if node.left:
                l.append(node.left)
            # 同上理
            if node.right:
                l.append(node.right)

        return res
