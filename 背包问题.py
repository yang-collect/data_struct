# 给你一个可装载重量为W的背包和N个物品，
# 每个物品有重量和价值两个属性。其中第i个物品的重量为wt[i]，价值为val[i]，
# 现在让你用这个背包装物品，最多能装的价值是多少？

def bag(W,N,wt,val):
    dp=[[0 for _ in range(N)] for _ in range(W)]
    