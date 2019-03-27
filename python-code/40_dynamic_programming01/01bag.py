def bag_max_weight(items_lst, capicity):
    n = len(items_lst)
    dp = [[-1] * (capicity + 1) for i in range(n)]
    # 不放入第一个物品
    dp[0][0] = 1
    # 放入第一个物品
    if items_lst[0] <= capicity:
        dp[0][items_lst[0]] = 1

    for i in range(1, n):
        for j in range(capicity + 1):
            # 不放入这个物品
            if dp[i - 1][j] == 1:
                dp[i][j] = 1
        for j in range(0, capicity + 1 - items_lst[i]):  # 保证放入物品后不超过容量
            if dp[i - 1][j] == 1:
                dp[i][j + items_lst[i]] = 1
    print(dp)
    for w in range(capicity, -1, -1):
        if dp[-1][w] == 1:
            print('max weight', w)
            break

    cur_weight = w
    # 选择方式
    picks = [0] * n
    for i in range(n - 1, -1, -1):
        if cur_weight - items_lst[i] >= 0 and dp[i - 1][cur_weight - items_lst[i]] == 1:
            picks[i] = 1
            cur_weight = cur_weight - items_lst[i]
    print(picks)


def bag_max_weight_optspace(items_lst, capicity):
    """
    将空间复杂度优化为 O(n)
    :param items_lst:
    :param capicity:
    :return:
    """
    n = len(items_lst)
    dp = [0] * (capicity + 1)
    # 不放入第一个物品
    dp[0] = 1
    # 放入第一个物品
    dp[items_lst[0]] = 1
    for i in range(1, n):
        for j in range(capicity - items_lst[i], -1, -1):
            if dp[j] == 1:
                dp[j + items_lst[i]] = 1
    for i in range(capicity, -1, -1):
        if dp[i] == 1:
            print('max weight', i)
            break

    cur_weight = i
    print(dp)
    # 选择方式
    picks = [0] * n
    for i in range(n - 1, -1, -1):
        print(picks, i, cur_weight)
        if cur_weight - items_lst[i] >= 0 and dp[cur_weight - items_lst[i]] == 1:
            picks[i] = 1
            cur_weight = cur_weight - items_lst[i]
    print(picks)


if __name__ == '__main__':
    items_lst = [3, 2, 1, 3, 6]
    capicity = 8
    bag_max_weight(items_lst, capicity)
    bag_max_weight_optspace(items_lst, capicity)
