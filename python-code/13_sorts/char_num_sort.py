from itertools import accumulate


class CountingSort(object):
    def index_from_char(self, char):
        flag = (char.isdigit(), char.isupper(), char.islower())
        for i, v in enumerate(flag):
            if v:
                return i

    def sort(self, a):
        cnt = [0] * 3
        for i in a:
            idx = self.index_from_char(i)
            cnt[idx] += 1

        cnt = list(accumulate(cnt))
        tmp = [0] * len(a)
        # 从后向前遍历，保证了排序的稳定性
        for i, v in enumerate(reversed(a)):
            v_idx = self.index_from_char(v)
            # 从累加结果中获得 index
            index = cnt[v_idx] - 1
            # 根据 index 在 tmp 中填充值
            tmp[index] = v
            # 累加结果减 1
            cnt[v_idx] -= 1
        a[:] = tmp


if __name__ == '__main__':
    a = ['a', 'A', '2']
    cs = CountingSort()
    cs.sort(a)
    print(a)
    a = ['D', 'a', 'F', 'B', 'c']
    cs = CountingSort()
    cs.sort(a)
    print(a)
