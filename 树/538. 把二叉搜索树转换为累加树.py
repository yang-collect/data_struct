# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
# 使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。

# 提醒一下，二叉搜索树满足下列约束条件：

# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# 累加器
sum=0

def covertBst(root):
    convert(root)
    return root

def convert(root):
    if  not root:
        return 
    # bst 反向遍历，得到降序数组，对降序数组进行累加、修改，才能满足 ： 节点 node 的新值等于原树中大于或等于 node.val 的值之和。
    # 访问右子树
    convert(root.right)
    # 累加
    sum+=root.val
    # 改变节点值
    root.val=sum
    # 访问左子树
    convert(root.righleft)


