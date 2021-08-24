# 给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

# 二叉树的根是数组 nums 中的最大元素。
# 左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
# 右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
# 返回有给定数组 nums 构建的 最大二叉树 。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_tree(nums):
    return bulid(nums, 0, len(nums)-1)

# 辅助函数


def bulid(nums, low, high):
   if low > high:
        return

    # 找到nums[low,high]最大元素以及位置
    max_value = nums.min()
    for i in range(low, high, 1):
        if max_value < nums[i]:
            index = i
            max_value = nums[i]

    # 节点值
    root = TreeNode(maxVal)
    # 左节点
    root.left = bulid(nums, low, index-1)
    # 右节点
    root.right = bulid(nums, index+1, high)

    return root
