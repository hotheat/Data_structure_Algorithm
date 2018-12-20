import numpy as np
import time


class BubbleSort(object):
    def sort(self, array):
        length = len(array)
        if length <= 1:
            return array
        for i in range(0, length):
            flag = False
            for j in range(0, length - i - 1):
                if array[j] > array[j + 1]:
                    # 交换操作
                    array[j], array[j + 1] = array[j + 1], array[j]
                    flag = True
            if flag is False:
                break
        return array


class InsertSort(object):
    def sort(self, array):
        length = len(array)
        if length <= 1:
            return array
        for i in range(1, length):
            value = array[i]
            j = i - 1
            # 从尾到头遍历
            while j >= 0:
                if array[j] > value:
                    # 移动操作
                    array[j + 1] = array[j]
                    j -= 1
                else:
                    break
            array[j + 1] = value
        return array


class SelectSort(object):
    def sort(self, array):
        length = len(array)
        if length <= 1:
            return array

        for i in range(length):
            minvalue = array[i]
            minidx = i
            for j in range(i + 1, length):
                if array[j] < minvalue:
                    # 这里是赋值操作，而非交换，如果是交换，时间复杂度会高
                    minvalue = array[j]
                    minidx = j
            # 只进行一次交换
            array[minidx], array[i] = array[i], array[minidx]
        return array


def cal_sort(sortfn, arr):
    stime = time.time()
    sorted_arr = sortfn.sort(arr)
    etime = time.time()
    return etime - stime, sorted_arr


def is_sorted(a, b):
    return (a == b).all()


def tetSort(n):
    types = ['all one', 'ordered', 're_order', 'random']
    for i in [BubbleSort, InsertSort, SelectSort]:
        arrs = [np.ones(n), np.arange(n), np.arange(n, 0, -1), np.random.randint(0, n, n)]
        for typ, arr in zip(types, arrs):
            arr_copy = arr.copy()
            sortfn = i()
            time, sorted_arr = cal_sort(sortfn, arr)
            print('{} time {} consumed {}'.format(i.__name__, typ, time))
            truesorted = sorted(arr_copy)
            assert is_sorted(sorted_arr, truesorted)


if __name__ == '__main__':
    n = 3000
    tetSort(n)
    # arrs = np.array([1, 2, 3, 4, 5, 6])
    # ss = SelectSort()
    # ss.sort(arrs)
