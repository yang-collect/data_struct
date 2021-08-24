# 根据一棵树的中序遍历与后序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 中序： 左-根-右
# 后序： 左-右-根
def bulidTree(inorder, postorder):
    return bulid(inorder, 0, len(inorder)-1,
                 postorder, 0, len(postorder)-1)


def bulid(inorder, inStart, inEnd, postorder, postStart, postEnd):
    if inStart > inEnd:
        return
    # 从后序中找到根节点的值
    value = postorder[postEnd]

    # 从中序中找到根节点位置
    for i in range(inStart, inEnd):
        if inorder[i] == value:
            index = i
            break

    root = TreeNode(value)

    # 构建左子树和右子树
    root.left = bulid(inorder, inStart, index-1, postorder, postStart, index-1)
    root.right = bulid(inorder, index+1, inEnd, postorder, index, postEnd-1)

    return root
