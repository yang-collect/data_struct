# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 说明：你不能倾斜容器。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/container-with-most-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 双指针

def maxArea(height):
    size = len(height)

    left, right = 0, size

    ans = 0
    # 遍历停止条件，左右指针相遇，即左右指针遍历一次数组
    while (left < right):

        area = min(height[left], height[right])*(right-left)

        ans = max(ans, area)
        # 将指向较大值的指针固定，移动较小值的指针：左指针相右移动，右指针相左移动
        if (height[left] <= height[right]):

            left += 1
        else:

            right -= 1

    return ans

# 相比于上一个版本的脚本，将min和max的步骤拆解了
    def maxArea(self, height: List[int]) -> int:
        # 左右指针端点处位置
        left, right = 0, len(height)-1
        ans = 0
        # 停止条件
        while (left < right):
            # 当左指针对应值较小时，以左指针对应的值为高度，宽度即为 (right-left)
            if height[left] <= height[right]:

                area = height[left]*(right-left)
                # 判断是否大于ans，大于ans时更新ans
                if ans < area:
                    ans = area
                left += 1
            else:
                # 同理，当右指针对应值较小时
                area = height[right]*(right-left)

                if ans < area:
                        ans = area
                right -= 1
        return ans
