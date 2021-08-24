# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
# 同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，
# 你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
# 你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Treenode:
    def __init__(self,val=None,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


class code:

    def serialize(self, root):
        sep=','
        null='#'
        s=''

        #  前序遍历 ，将其转换为字符串
        def travse(root,s):
            if not root:
                s+=null+sep
                return 
            
            s+=str(root.val)+sep

            travse(root.left,s)
            travse(root.right,s)
        
        travse(root,s)
        return s

    # 反序列化
    def deserialize(self,data):
        nodes=[]
        for i in data.split(','):
            nodes.append(i)

        return self.node(nodes)
    
    def node(self,nodes):
        first=nodes.pop(0)

        if not first:
            return 
        # 用前序或者后序是因为可以确定节点在值
        root=Treenode(nodes)
        root.left=node(self,nodes)
        root.right=node(self,nodes)
        return root



def __main__():
    code=code()
    print(code.deserialize([1,2,3,'#','#',4,5]))