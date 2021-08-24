def fib(n):
    # 构造一个备忘录来记录状态转移结果
    m = [0 for _ in range(n+1)]
    # bad case
    m[1] = 1
    for i in range(2, n+1):
        # 状态转移方程
        m[i] = m[i-1]+m[i-2]
    return m[n]
