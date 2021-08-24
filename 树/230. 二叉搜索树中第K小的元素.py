# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

# bst(二叉搜索树)： 每一个左子树值都小于节点值，节点值小于右子树值；对于每个节点左右子树都是bst
# BST 的中序遍历结果是有序的（升序）

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

rank=0
def kthSmallest(root,k):
    return  travse(root,k)

def travse(root,k):
    if  not root:
        return 
 
    # 中序遍历
    travse(root.left,k)
    rank+=1
    if rank==k:
        res=root.val
        return res
    
    travse(root.right,k)



