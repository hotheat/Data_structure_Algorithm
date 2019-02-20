def full_permutation(array, length, depth):
    print_permutation(array, length, depth)


def print_permutation(array, length, depth):
    # print('depth,', depth)
    """
    思路：
    如果确定了最后一位数据，就变成求解剩下 n-1 个数据的全排列问题
    最后一位数据的取值有 n 种，所有 n 个数据的全排列问题变成 n 个 "n-1 子问题的全排列"
    """
    if depth == 1:
        print(' '.join(map(str, array)))

    for i in range(depth):
        array[i], array[depth - 1] = array[depth - 1], array[i]
        print_permutation(array, length, depth - 1)
        array[depth - 1], array[i] = array[i], array[depth - 1]


array = [1, 2, 3]
full_permutation(array, len(array), len(array))
