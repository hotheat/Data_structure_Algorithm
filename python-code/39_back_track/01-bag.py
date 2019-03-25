def bag01(capcity, cur_weight, cur_value, item_idx, item_lst):
    """
    回溯法解决 01 背包问题，穷举，每个背包都有选或不选两种选择
    :param capcity: 背包容量
    :param cur_weight: 当前背包重量
    :param item_idx: 当前物品
    :param item_lst: 物品的重量和价值
    :return:
    """
    if item_idx == len(item_lst) or cur_weight == capcity:
        global max_value, opt_pick
        if cur_value > max_value:
            max_value = cur_value
            opt_pick = picks.copy()
        return

    else:
        # 不选
        picks[item_idx] = 0
        bag01(capcity, cur_weight, cur_value, item_idx + 1, item_lst)
        item_weight = item_lst[item_idx][0]
        item_value = item_lst[item_idx][1]
        # 如果不超过容量，再进行选择
        if cur_weight + item_weight <= capcity:
            picks[item_idx] = 1
            bag01(capcity, cur_weight + item_weight,
                  cur_value + item_value, item_idx + 1, item_lst)


if __name__ == '__main__':
    # weight, value
    items_lst = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    capicity = 8
    picks = [0] * len(items_lst)
    max_value = 0
    opt_pick = picks
    bag01(capicity, 0, 0, 0, items_lst)
    print('best_pick: ', opt_pick)
    print('max value: ', max_value)
