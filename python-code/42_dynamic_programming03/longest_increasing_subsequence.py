count = 0


def longest_increasing(prev, num_idx, cur_length, num_lst):
    """
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


if __name__ == '__main__':
    prev = max_length = float('-inf')
    num_lst = [2, 9, 3, 6, 5, 1, 7]
    mem = {}
    print(longest_increasing(prev, 0, 0, num_lst))
    print(max_length)
