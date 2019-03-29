from pprint import pprint


def min_coin_number(cur_count, cur_value, total_value, coin_lst):
    """
    回溯法思路：
    假设硬币面值 1，3，5，总额是 9。先全部用面值为 1 的硬币，再逐渐减少面值为 1 的硬币，
    换成面值为 3 的硬币，
    :return:
    """
    global min_count
    # 符合面值要求
    if cur_value == total_value:
        min_count = min(cur_count, min_count)

    for v in coin_lst:
        # 遍历所有的硬币面额
        if cur_value + v <= total_value:
            min_coin_number(cur_count + 1, cur_value + v, total_value, coin_lst)


def min_coin_count_onedim1(coin_lst, total_value):
    """
    状态转移表法解决
    dp[i] 代表 total_value 为 i 的索引时所需的最少硬币数量
    状态转移方方程 min_num  = min(min_num, dp[i-coins[j]] + 1)
    i-coins[j] 是总钱数减去当前硬币面额
    """
    # mem 是个数组，代表 value 分别是下标时所需要的最小硬币数
    dp = [0] * (total_value + 1)
    # value 为 0 时，需要 0 个硬币
    dp[0] = 0
    for i in range(1, total_value + 1):
        # 每次把最小值初始化成最大值
        min_num = float('inf')
        for v in coin_lst:
            if i >= v:
                min_num = min(min_num, 1 + dp[i - v])
        dp[i] = min_num
    print(dp)
    return dp[-1]


def min_coin_count_onedim2(coin_lst, total_value):
    """
    状态转移表法解决
    状态转移方方程 dp[i]  = min(dp[i], dp[i-coins[j]] + 1)
    i-coins[j] 是总钱数减去当前硬币面额
    """
    # mem 是个数组，代表 value 分别是下标时所需要的最小硬币数
    # 初始化方式：假设有面值为 1 的硬币，面值为 total_value 时，需要 total_value 个
    dp = [total_value + 1] * (total_value + 1)
    # value 为 0 时，需要 0 个硬币
    dp[0] = 0
    for i in range(1, total_value + 1):
        # 每次把最小值初始化成 最大值
        for v in coin_lst:
            if i >= v:
                dp[i] = min(dp[i], 1 + dp[i - v])
    print(dp)
    return dp[-1]


def min_coin_count_twodim(coin_lst, total_value):
    """
    dp[i][j] 代表只用前 i 种硬币构成面值为 j 所需的最小硬币数
    dp[i][j] = min(dp[i][j], dp[i][j-coins[i]] + 1)
    不加入一个硬币 i 时，构成的面额是 j-coins[i]，如果要达到 j，那再需要一个硬币就可以
    :param coin_lst:
    :param total_value:
    :return:
    """
    # 初始化
    # 假设面值为 0，需要无穷个硬币，假设总价值为 0，只需要 0 个硬币
    n = len(coin_lst)
    dp = [[float('inf')] * (total_value + 1) for i in range(n + 1)]
    for i in dp:
        i[0] = 0
    for r in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            for coin in coin_lst:
                dp[r][col] = min(dp[r][col], dp[r][col - coin] + 1)

    pprint(dp)
    return dp[-1][total_value]


if __name__ == '__main__':
    coins = [2, 3, 5]
    total_val = 13
    min_count = float('inf')
    min_coin_number(0, 0, total_val, coins)
    print(min_count)
    print(min_coin_count_onedim1(coins, total_val))
    print(min_coin_count_onedim2(coins, total_val))
    print(min_coin_count_twodim(coins, total_val))
