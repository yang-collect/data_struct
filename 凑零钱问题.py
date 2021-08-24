# 给你k种面值的硬币，面值分别为c1, c2 ... ck，每种硬币的数量无限，
# 再给一个总金额amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1 。

def coinChange(coins,amount):
    if amount==0:
        return 0

    # 用一个字典记录当前的值以及需要多少个硬币
    memo={}
    def dp(n):
        '''
                            0, n=0
            dp[n] =     -1,n<0
                            min(dp[n-coin]+1,dp[n-1])

        '''
        # 查找备忘录
        if n in memo: return memo[n]

        # bad case
        if n==0: return 0
        if n<0 : return -1

        res=float('INF')
        for coin in coins:
            subproblem=dp(n-coin)
            if subproblem==1: continue
            res=min(1+subproblem,res)

        # 记入备忘录
        memo[n] = res if res != float('INF') else -1
        return memo[n]
    return  dp[amount]


def coinChange1(coins,amount):
    if  amount==0: return 0

    memo=[]
    
