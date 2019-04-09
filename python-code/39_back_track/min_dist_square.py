def min_dist_square(row, col, dist, weight_matrix):
    """
    回溯算法实现从权重矩阵中找到最小路径，先遍历到最下面，再遍历最右边
    :param row:
    :param col:
    :param dist:
    :param weight_matrix:
    :return:
    """
    if row == len(weight_matrix) - 1 and col == len(weight_matrix) - 1:
        global min_d
        min_d = min(dist, min_d)
        return

    if row < len(weight_matrix) - 1:  # 向下走，更新 row+1, col
        min_dist_square(row + 1, col, dist + weight_matrix[row][col], weight_matrix)

    if col < len(weight_matrix) - 1:  # 向右走，更新 row, col+1
        min_dist_square(row, col + 1, dist + weight_matrix[row][col], weight_matrix)


if __name__ == '__main__':
    min_d = float('inf')
    dist_lst = [[1, 3, 5, 9],
                [2, 1, 3, 4],
                [5, 2, 6, 7],
                [6, 8, 4, 3]]

    min_dist_square(0, 0, 0, dist_lst)
    print(min_d)
