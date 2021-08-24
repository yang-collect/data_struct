# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        # bfs层序遍历加双端队列
        search=collections.deque([root])
        res=[]
        while search:
            mid=[] 
            for _ in range(len(search)):
                node=search.popleft() # 弹出栈底元素，先进先出
                mid.append(node.val)
                if node.left: search.append(node.left)
                if node.right: search.append(node.right)
            # 是偶数的时候取逆序
            res.append(mid[::-1] if len(res)%2 else mid)
        
        return res