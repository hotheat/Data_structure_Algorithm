from pprint import pprint


def leven_dist_traceback(str1, str2):
    """
    回溯法求莱文斯坦距离
    :param str1:
    :param str2:
    :return:
    """
    length1 = len(str1)
    length2 = len(str2)

    def lwsdist(i, j, edist):
        if i == length1 or j == length2:
            global min_dist
            if i < length1:
                edist += length1 - i
            if j < length2:
                edist += length2 - j
            min_dist = min(edist, min_dist)
            return

        # 如果两个字符匹配
        if str1[i] == str2[j]:
            lwsdist(i + 1, j + 1, edist)
        # 如果两个字符不匹配，有三种情况
        else:
            # 删除 a[i] 或在 b[j] 前面添加 a[i]
            lwsdist(i + 1, j, edist + 1)
            # 删除 b[j] 或在 a[i] 前面添加 b[j]
            lwsdist(i, j + 1, edist + 1)
            # 将 a[i] 和 b[j] 替换为相同字符
            lwsdist(i + 1, j + 1, edist + 1)

    return lwsdist(0, 0, 0)


def leven_dist_dp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * n for i in range(m)]
    # 填充第 0 行
    for i in range(n):
        if str2[i] == str1[0]:
            dp[0][i] = i
        elif i != 0:
            dp[0][i] = dp[0][i - 1] + 1
        else:
            dp[0][i] = 1
    # 填充第 0 列
    for j in range(m):
        if str1[j] == str2[0]:
            dp[j][0] = j
        elif j != 0:
            dp[j][0] = dp[j - 1][0] + 1
        else:
            dp[j][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            if str1[i] == str2[j]:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    return dp[-1][-1]


if __name__ == '__main__':
    str1 = 'itcmu'
    str2 = 'mtacnu'
    min_dist = float('inf')
    leven_dist_traceback(str1, str2)
    print(min_dist)
    pprint(leven_dist_dp(str1, str2))
