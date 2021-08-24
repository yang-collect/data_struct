# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def flatten(root):
    if  not root:
        return 
    

    # 拉伸左右子节点
    flatten(root.left)
    flatten(root.right)

    # 记录左右子树
    left=root.left
    right=root.right

    # 将左子树作为右子树
    root.left=None
    root.right=left

    # 将原来的右子树接到右子树的末端
    # root作为
    p=root
    while p.right:
        p=p.right
    p.right=right
