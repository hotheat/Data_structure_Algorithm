from itertools import accumulate


class CountingSort(object):
    def sort(self, a):
        cnt = [0] * (max(a) + 1)
        for i in a:
            cnt[i] += 1
        cnt = list(accumulate(cnt))
        tmp = [0] * len(a)
        for v in a:
            # 从累加结果中获得 index
            index = cnt[v] - 1
            # 根据 index 在 tmp 中填充值
            tmp[index] = v
            # 累加结果减 1
            cnt[v] -= 1
        a[:] = tmp


if __name__ == '__main__':
    a = [2, 5, 2, 3, 3]
    cs = CountingSort()
    cs.sort(a)
    print(a)
    a2 = [1, 1, 1, 1]
    cs.sort(a2)
    print(a2)
