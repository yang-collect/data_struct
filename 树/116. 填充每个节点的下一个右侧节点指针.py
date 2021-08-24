# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

# 初始状态下，所有 next 指针都被设置为 NULL。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


def connect(root):
    if  not root :
        return root
    # 借助一个辅助函数完成将相邻节点连接
    connect_2_node(root.left,root.right)
    return root

def connect_2_node(node1,node2):
    if  not node1 or not node2:
        return 
    # 连接node1、node2
    node1.next=node2

    # 连接node1、node2的左右子节点
    connect_2_node(node1.left,node1.right)
    connect_2_node(node2.left,node2.right)

    # 连接node1的右节点和node2的左节点
    connect_2_node(node1.right,node2.left)
