matrix_num = 8
# solution_lst 索引代表棋子所在行，值代表棋子所在列
solution_lst = [0] * matrix_num
solution_count = 0


def eight_queen(row):
    if row == matrix_num:
        global solution_count
        solution_count += 1
        # 成功的话就是一种方法
        print(solution_lst)
        return
    # 每行都有 8 种方法
    for col in range(matrix_num):
        if is_valid(row, col):
            solution_lst[row] = col  # 棋子放在第 r 行第 c 列
            # 每行放一个
            eight_queen(row + 1)


def is_valid(row, col):
    """
    is_valid 函数检查当前行之上的所有行，
    在竖直列，左对角线，右对角线上是否有棋子
    """
    leftup, rightup = col - 1, col + 1

    for i in range(row - 1, -1, -1):
        global solution_lst
        # 第 i 行第 c 列有棋子
        if solution_lst[i] == col:
            return False
        # 左上方有棋子
        elif leftup >= 0 and solution_lst[i] == leftup:
            return False
        # 右上方有棋子
        elif rightup < matrix_num and solution_lst[i] == rightup:
            return False
        leftup -= 1
        # 右上方列数加 1
        rightup += 1
    return True

    # i = 0
    # while i < row:
    #     # 同行
    #     if solution_lst[i] == col:
    #         return False
    #     # 对角线
    #     if row - i == abs(col - solution_lst[i]):
    #         return False
    #     i += 1
    # return True


if __name__ == '__main__':
    eight_queen(0)
    print(solution_count)
