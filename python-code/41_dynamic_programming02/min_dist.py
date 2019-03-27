from itertools import accumulate


def min_dist_table(matrix):
    """
    状态转移表法实现最小路径问题
    :param matrix:
    :return:
    """
    n = len(matrix)
    table = [[0] * n for i in range(n)]
    first_row = list(accumulate(matrix[0]))
    first_col = list(accumulate([i[0] for i in matrix]))
    table[0] = first_row
    for i, c in enumerate(table):
        c[0] = first_col[i]

    for r in range(1, n):
        for c in range(1, n):
            table[r][c] = min(table[r][c - 1] + matrix[r][c], table[r - 1][c] + matrix[r][c])

    return table[-1][-1]


def min_dist_formula(matrix):
    n = len(matrix)
    table = [[0] * n for i in range(n)]

    def min_dist(i, j):
        # 初始化
        if i == j == 0: return matrix[0][0]
        # 记忆化
        if table[i][j] != 0:
            return table[i][j]

        min_left = float('inf') if j == 0 else min_dist(i, j - 1)
        min_up = float('inf') if i == 0 else min_dist(i - 1, j)
        return matrix[i][j] + min(min_left, min_up)

    return min_dist(n - 1, n - 1)


if __name__ == '__main__':
    dist_lst = [[1, 3, 5, 9],
                [2, 1, 3, 4],
                [5, 2, 6, 7],
                [6, 8, 4, 3]]
    print(min_dist_table(dist_lst))
    print(min_dist_formula(dist_lst))
