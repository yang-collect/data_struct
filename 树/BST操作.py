# 在 BST 中搜索一个数
def isInTree(root, target):
    # bad case
    if not val:
        return False
    # 二分搜索
    if root.val == target:
        return True
    elif root.val > target:
        isInTree(root.right, target)
    else:
        isInTree(root.left, target)

# 在 BST 中插入一个数


def insert(root, target):
    if not root:
        return TreeNode(target)

    if root.val < target:
        insert(root.left, target)

    if root.val > target:
        insert(root.right, target)

'''
# 标准模板

def deal(root, target):
    if not root:
        return  # deal1

    if root.val == target:
        # deal2
    elif root.val > target:
        deal(root.right, target)
    else:
        deal(root.left, target)
'''

# 删除一个节点

def delete(root, target):
    if not root:
        return
    if root.val == target:
        # 当左右子节点都为空时，返回空
        if not root.left and not root.right:
            return
        # 当左节点或右节点为空时，返回另一个节点
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            # 有两个子节点，麻烦了，为了不破坏 BST 的性质，A必须找到左子树中最大的那个节点，
            # 或者右子树中最小的那个节点来接替自己,这里先写第二种
            mininode = getmin(root.right)
            root.val = mininode.val
            delete(root.right, mininode.val)
    elif root.val > target:
        delete(root.right, target)
    else:
        delete(root.left, target)
    return root


def mininode(root):
    # 由于bst本身的性质，左子树是较小的，故只需遍历到左子树的最末节点即为最小值
    while root.left:
        root = root.left
    return root

