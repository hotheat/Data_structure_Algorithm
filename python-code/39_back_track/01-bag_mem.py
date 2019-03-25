count = 0


def bag_mem(capcity, cur_weight, item_idx, item_lst):
    """
    利用记忆化递归优化回溯算法解决 01 背包问题中的重复计算问题
    item list 中只有重量，要求选择能够装入背包的最大重量
    从递归树的来看，递归树中的每个节点 f(i, cw)，i 代表当前物品是否选择，cw 代表当前背包的重量
    如果 f(i, cw) 出现过，那么不必再重复计算
    :return:
    """
    global count
    count += 1
    if item_idx == len(item_lst) or cur_weight == capcity:
        global max_weight, opt_pick
        if cur_weight > max_weight:
            max_weight = cur_weight
            opt_pick = picks.copy()
        return
    # 记忆化
    if (item_idx, cur_weight) in mem:
        return
    mem[(item_idx, cur_weight)] = True

    picks[item_idx] = 0
    bag_mem(capcity, cur_weight, item_idx + 1, item_lst)
    if cur_weight + item_lst[item_idx] <= capcity:
        picks[item_idx] = 1
        bag_mem(capcity, cur_weight + item_lst[item_idx], item_idx + 1, item_lst)


if __name__ == '__main__':
    item_lst = [3, 2, 1, 2, 4, 6]
    capcity = 8
    max_weight = 0
    mem = {}
    opt_pick = picks = [0] * len(item_lst)
    bag_mem(capcity, 0, 0, item_lst)
    print('max weight', max_weight)
    print('best choice', opt_pick)
    print('count', count)