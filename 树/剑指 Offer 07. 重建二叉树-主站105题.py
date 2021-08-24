# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        前序遍历： 根-左-右
        中序遍历： 左-根-右
        后续遍历： 左-右-根
        '''
        map_index={value:index for index,value in enumerate(inorder)}

        def build(instart,inend,prestart,preend):
            '''
                
            ''' 
            if prestart>preend: return None
            
            value=preorder[prestart]
            index=map_index[value]
            root=TreeNode(value)
            size=index-instart
            # 左节点
            root.left=build( instart, index-1,  prestart+1, prestart+size)
            # 右节点
            root.right=build( index+1, inend,  prestart+size+1, preend)
                
            return root
        
        
        return build(0,len(inorder)-1,0,len(preorder)-1)