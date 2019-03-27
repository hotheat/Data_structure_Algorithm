def bag_max_value(items_lst, capicity):
    """
    :param items_lst: （weight, value）
    :param capicity:
    :return:
    """
    n = len(items_lst)
    dp = [[-1] * (capicity + 1) for i in range(n)]
    dp[0][0] = 0
    # 加入第一个物品后的价值
    dp[0][items_lst[0][0]] = items_lst[0][1]

    for i in range(1, n):
        for j in range(capicity + 1):
            # 不加入物品后的价值
            if dp[i - 1][j] >= 0:
                dp[i][j] = dp[i - 1][j]

        for j in range(capicity - items_lst[i][0], -1, -1):
            if dp[i - 1][j] >= 0:
                # 加入后的价值是遍历每个位置后，加入该商品的价值最大值
                dp[i][j + items_lst[i][0]] = max(dp[i][j + items_lst[i][0]],
                                                 dp[i - 1][j] + items_lst[i][1])

    max_value = -1
    for i in range(capicity, -1, -1):
        if dp[-1][i] > max_value:
            cur_weight = i
            max_value = dp[-1][i]
    print('cur weight', cur_weight)
    print('max value', max_value)
    # 打印选择过程
    picks = [0] * n
    for i in range(n - 1, -1, -1):
        if cur_weight - items_lst[i][0] >= 0 and max_value - items_lst[i][1] == dp[i - 1][cur_weight - items_lst[i][0]]:
            picks[i] = 1
            max_value = max_value - items_lst[i][1]
            cur_weight = cur_weight - items_lst[i][0]

    print('picks', picks)


def bag_max_value_optspace(items_lst, capicity):
    n = len(items_lst)
    dp = [-1] * (capicity + 1)
    # 是否加入第一个物品
    dp[0] = 0
    dp[items_lst[0][0]] = items_lst[0][1]

    for i in range(1, n):
        for j in range(capicity - items_lst[i][0], -1, -1):
            if dp[j] >= 0:
                v = dp[j + items_lst[i][0]]
                if dp[j] + items_lst[i][1] > v:
                    dp[j + items_lst[i][0]] = dp[j] + items_lst[i][1]

    max_value = -1
    for i, v in enumerate(dp):
        if v > max_value:
            cur_weight = i
            max_value = v
    print('current weight', cur_weight)
    print('max value', max_value)

    
if __name__ == '__main__':
    # weight, value
    items_lst = [(3, 5), (2, 2), (1, 4), (1, 2), (3, 10)]
    capicity = 8
    bag_max_value(items_lst, capicity)
    bag_max_value_optspace(items_lst, capicity)
