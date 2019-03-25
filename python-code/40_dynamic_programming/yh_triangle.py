def yh_triangle(nums):
    """
    dp 的表格是个下三角形
    :param nums:
    :return:
    """
    n = len(nums)
    dp = [[-1] * n for i in range(n)]
    dp[0][0] = nums[0][0]
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + nums[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + nums[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + nums[i][j], dp[i - 1][j] + nums[i][j])
    return min(dp[-1])


def yh_triangle_optspace(nums):
    n = len(nums)
    dp = [-1] * n
    dp[0] = nums[0][0]

    for i in range(1, n):
        for j in range(i, -1, -1):
            if j == 0:
                dp[j] = dp[j] + nums[i][j]
            elif j == i:
                dp[j] = dp[j - 1] + nums[i][j]
            else:
                dp[j] = min(dp[j - 1] + nums[i][j], dp[j] + nums[i][j])
    return min(dp)





if __name__ == "__main__":
    nums = [[3], [2, 6], [5, 4, 2], [6, 0, 3, 2]]
    print(yh_triangle(nums))
    print(yh_triangle_optspace(nums))
