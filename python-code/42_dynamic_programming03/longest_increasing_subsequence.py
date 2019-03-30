count = 0


def longest_increasing(prev, num_idx, cur_length, num_lst):
    """
    https://www.bilibili.com/video/av38027355/
    回溯法解决最长递增子序列问题
    和 01 背包问题类似，每个数据都有选和不选两种选择。
    如果当前数字比前面数字（prev）大，那就选择，否则不选
    :return:
    """
    if num_idx == len(num_lst):
        global max_length
        max_length = max(max_length, cur_length)
        return

    longest_increasing(prev, num_idx + 1, cur_length, num_lst)
    # 如果比前面的数字大，length + 1
    if num_lst[num_idx] > prev:
        prev = num_lst[num_idx]
        longest_increasing(prev, num_idx + 1, cur_length + 1, num_lst)


def longest_increasing_dp(num_lst):
    """
    dp[i] 记录代表序列长度为 i 时的最长递增子序列，时间复杂度为 O(n^2)
    https://www.youtube.com/watch?v=7DKFpWnaxLI
    :param num_lst:
    :return:
    """
    dp = [1] * (len(num_lst))
    for i in range(1, len(num_lst)):
        for j in range(i):
            if num_lst[i] > num_lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


if __name__ == '__main__':
    prev = max_length = float('-inf')
    num_lst = [2, 9, 3, 6, 5, 1, 7]
    num_lst = [1, 2, 3, 4, 5, 6]
    longest_increasing(prev, 0, 0, num_lst)
    print(max_length)
    longest_increasing_dp(num_lst)
