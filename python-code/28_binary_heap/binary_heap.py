import math


class BinaryHeap(object):
    """
    大顶堆
    """
    def __init__(self, data=[], capicity=100):
        self.init_data(data)
        self.capicity = capicity
        assert self.length <= self.capicity, 'Heap init ovepsize'

    def init_data(self, data):
        if not data:
            data.append(None)
        else:
            data[1:] = data
            data[0] = None
        self._data = data

    @property
    def length(self):
        return len(self._data) - 1

    def parent_idx(self, index):
        return index // 2

    def left_childidx(self, index):
        return index * 2

    def right_childidx(self, index):
        return index * 2 + 1

    def parant(self, index):
        pidx = self.parent_idx(index)
        if pidx > 0:
            return self._data[pidx]
        else:
            return None

    def left_child(self, index):
        lidx = self.left_childidx(index)
        # 非叶子节点
        if lidx <= self.length:
            return self._data[lidx]
        else:
            return None

    def right_child(self, index):
        ridx = self.right_childidx(index)
        # 非叶子节点
        if ridx <= self.length:
            return self._data[ridx]
        else:
            return None

    def heapify_down2top(self, index):
        pidx = self.parent_idx(index)
        p = self.parant(index)
        while pidx > 0 and self._data[index] > p:
            self._data[index], self._data[pidx] = self._data[pidx], self._data[index]
            index = pidx
            pidx = self.parent_idx(index)
            p = self.parant(index)

    def heapify_top2down(self, n, index):
        while True:
            lc_ix, rc_ix = self.left_childidx(index), self.right_childidx(index)
            lc, rc = self.left_child(index), self.right_child(index)
            max_pos = index
            if lc_ix <= n and lc and self._data[index] < lc:
                max_pos = lc_ix
            if rc_ix <= n and rc and self._data[max_pos] < rc:
                max_pos = rc_ix
            # 堆顶元素最大
            if max_pos == index:
                break
            self._data[max_pos], self._data[index] = self._data[index], self._data[max_pos]
            index = max_pos

    def insert(self, element):
        if self.length + 1 >= self.capicity:
            return
        else:
            self._data.append(element)
            last_idx = self.length
            self.heapify_down2top(last_idx)

    def remove_max(self):
        # 堆中没有数据
        if self.length == 0:
            return -1
        # 把末位元素移至堆顶
        last = self._data.pop()
        if self.length:
            self._data[1] = last
            self.heapify_top2down(self.length, 1)
        else:
            return None

    def build_heap(self):
        for i in range(self.length // 2, 0, -1):
            self.heapify_top2down(self.length, i)

    def sort(self):
        """
        sort 共分两步，堆化和排序
        堆化采用从下往上的方法，从非叶子节点开始，在堆中，下标从 (n//2+1) 到 n 全部是叶子节点
        排序时，先将堆顶元素与末位元素交换，元素计数减一，然后堆化，循环操作，直至堆中只剩一个元素
        """
        self.build_heap()
        n = self.length
        while n > 1:
            self._data[1], self._data[n] = self._data[n], self._data[1]
            n -= 1
            self.heapify_top2down(n, 1)

    def _draw_heap(self):
        n = 0
        res = ''
        if self.length == 0:
            return 'empty heap'
        for i, v in enumerate(self._data[1:], 1):
            if n <= int(math.log2(i)) < n + 1:
                res = ','.join((res, str(v)))
            elif i > 0:
                n += 1
                res = '\n'.join((res, str(v)))
        return res

    def __str__(self):
        return self._draw_heap()


if __name__ == '__main__':
    bp = BinaryHeap()
    for i in range(8, 25):
        bp.insert(i)
    for i in [4, 18]:
        bp.insert(i)
    print(bp.length)
    print(bp)
    for i in range(19):
        bp.remove_max()
    print('全部移除后 bp', bp)
    l = list(range(10, 18))
    import random

    random.seed(1)
    random.shuffle(l)
    print(l)
    bp = BinaryHeap(l)
    bp.sort()
    print(bp)
