# 检查root.val是否在[root.min,root.max]中
def check_bst(root):
    return  check(root,None,None)

def check(root,min,max):
#  bad case
    if not root:
        return True
    # 若 root.val 不符合 max 和 min 的限制，说明不是合法 BST
    if  min and root.val<=min.val:
        return False
    if  max and root.val>=max.val:
        return False
    # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
    return check(root.left,min,root) and check(root.right,root,max)
    
