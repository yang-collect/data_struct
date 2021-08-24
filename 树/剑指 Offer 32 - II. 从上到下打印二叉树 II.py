
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res,l=[],collections.deque([root])
        while l:
            tmp=[] # 记录每一层的结果
            for _ in range(len(l)): # 遍历一层
                node=l.popleft()
                tmp.append(node.val)
                if node.left: l.append(node.left)
                if node.right: l.append(node.right)
            res.append(tmp)
        
        return res