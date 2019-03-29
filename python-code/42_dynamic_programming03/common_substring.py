from pprint import pprint


def common_substring_dp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * n for i in range(m)]
    # 填充第 0 行
    for i in range(n):
        if str2[i] == str1[0]:
            dp[0][i] = 1
        elif i != 0:
            dp[0][i] = dp[0][i - 1]
        else:
            dp[0][i] = 0

    # 填充第 0 列
    for j in range(m):
        if str1[j] == str2[0]:
            dp[j][0] = 1
        elif j != 0:
            dp[j][0] = dp[j - 1][0]
        else:
            dp[j][0] = 0

    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    pprint(dp)
    return dp[-1][-1]


if __name__ == '__main__':
    str1 = 'mitcmu'
    str2 = 'mtacnu'
    max_dist = float('-inf')
    pprint(common_substring_dp(str1, str2))
