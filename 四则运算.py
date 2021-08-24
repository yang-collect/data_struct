# 输入一个表达式（用字符串表示），求这个表达式的值。
# 保证字符串中的有效字符包括[‘0’-‘9’],‘+’,‘-’, ‘*’,‘/’ ,‘(’， ‘)’,‘[’, ‘]’,‘{’ ,‘}’。且表达式一定合法。

# 大中括号的实际意义与小括号一样，只是运算写法不同，优先级和运算的意义是一样的

def pri(a):
    if a == '(':
        return 1
    elif a == '+' or a == '-':
        return 2
    elif a == '*' or a == '/':
        return 3

w={'(':1,'+':2,'-':2,'*':3,'/':3}
def cal(a,b,c):
    if c == '-':
        return int(a) - int(b)
    elif c == '+':
        return  int(a) + int(b)
    elif c == '*':
        return int(a) * int(b)
    elif c == '/':
        return int(a)//int(b)
while True:
    try:
        s = input().strip()
        data = []
        count = []
        s = s.replace('[','(')
        s = s.replace('{','(')
        s = s.replace('}',')')
        s = s.replace(']',')')
        i = 0
        while i < len(s):
            # 将一个个数字加入data中
            if s[i].isdigit():   #处理数字
                j = i
                while j < len(s) and s[j].isdigit() :
                    j = j + 1
                data.append(s[i:j]) # 由于数字不止一位，故使用双指针来实现取数操作
                i = j # 遍历完当前数字后移动左指针至当前右指针处
            elif s[i] in ['+','-','*','/']: 
                if s[i] == '-':   #处理负数的情况，在-前面加上0
                    if i==0 or not s[i-1].isdigit() and s[i-1]!=')':
                        s = list(s)
                        s.insert(i,'0')
                        s = ''.join(s)
                        continue
                # 当计算符那个列表为空时，直接加入当前计算符
                if not count:
                    count.append(s[i])
                else:
                    # 若当前计算符优先级高于运算符列表的栈顶，将当前运算符压入运算栈
                    if w[s[i]] > w[count[-1]]:
                        count.append(s[i])
                    else:
                        # 当运算栈不空且当前运算的优先级不高于栈顶，
                        # pop出栈顶计算符放入data中，将当前运算压入栈
                        while count and w[s[i]] <= w[count[-1]]:
                            sym = count.pop()
                            data.append(sym)
                        count.append(s[i])
                i = i+ 1
            else:
                if s[i] == '(':
                    count.append(s[i])
                else:
                    while count[-1] != '(':
                        data.append(count.pop())
                    count.pop()
                i = i + 1
        while count:
            data.append(count.pop())
        #print(data)
        j = 0
        while len(data) != 1:
            try:
                fl = int(data[j])
                j += 1
            except:
                t1 = data.pop(j)
                t2 = data.pop(j-1)
                data[j-2] = str(cal(data[j-2],t2,t1))
                j = j - 1
        print(data[0])
    except:
        break
