# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 前序：根-左-右
# 中序： 左-根-右

def bildTree(preorder, inorder):
    return build(preorder, 0, len(preorder)-1,
                         inorder, 0, len(inorder)-1)

def build(preorder,preStart,preEnd,inorder,inStart,inEnd):
    if   preStart>preEnd:
        return None
    # 找到根节点的值
    value=preorder[preStart]
    # 在中序中找到根节点位置，以定位左子树
    for i in range(inStart,inEnd):
        if  inorder[i]==value:
            index=i
            break
    
    root=TreeNode(value)
    #  添加左右子树
    # 左子树
    root.left=build(preorder,preStart+1,index,
                    inorder,inStart,index-1)
    # 右子树
    root.right=bulid(preorder,index+1,preEnd,
                    inorder,index+1,inEnd)

    return root

