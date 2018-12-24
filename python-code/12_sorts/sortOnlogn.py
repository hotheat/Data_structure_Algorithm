import numpy as np
import time


class MergeSort_1(object):
    """
    merge 合并函数
    """

    def sort(self, array):
        length = len(array)
        self.merge_sort(array, 0, length - 1)
        return array

    def merge_sort(self, array, low, high):
        if low >= high:
            return
        # low + high，如果 low 和 high 都比较大时，可能溢出
        mid = low + (high - low) // 2
        # 除以 2 也可以用位操作，右移 n 位，相当于除以 2**n
        # mid = low + (high - low) >> 1
        self.merge_sort(array, low, mid)
        self.merge_sort(array, mid + 1, high)

        self.merge(array, low, mid, high)

    def merge(self, array, low, mid, high):
        i, j = low, mid + 1
        tmp = []
        while i <= mid and j <= high:
            if array[i] <= array[j]:
                tmp.append(array[i])
                i += 1
            else:
                tmp.append(array[j])
                j += 1
        # 如果 i 超过 mid 坐标，取 [j, high]；如果没超过，取 [i, mid]
        if i <= mid:
            start, end = i, mid
        else:
            start, end = j, high

        tmp.extend(array[start: end + 1])
        array[low:high + 1] = tmp


class MergeSort_2(object):
    def sort(self, array):
        return self.merge_sort(array)

    def merge(self, left, right):
        tmp = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1
        while i < len(left):
            tmp.append(left[i])
            i += 1
        while j < len(right):
            tmp.append(right[j])
            j += 1
        return tmp

    def merge_sort(self, array):
        if len(array) <= 1:
            return array
        else:
            mid = len(array) // 2
            left = self.merge_sort(array[:mid])
            right = self.merge_sort(array[mid:])
            return self.merge(left, right)


class QuickSortNoinplace_1(object):
    """
    有 partition 分区函数
    """

    def sort(self, array):
        self.quick_sort(array, 0, len(array) - 1)
        return array

    def patition(self, array, low, high):
        pivot = array[high]
        left, right = [], []
        j = low
        for i in range(low, high):
            if array[i] <= pivot:
                left.append(array[i])
                j += 1
            else:
                right.append(array[i])
        array[low:high + 1] = left + [pivot] + right
        return j

    def quick_sort(self, array, low, high):
        if low >= high:
            return
        else:
            p = self.patition(array, low, high)
            self.quick_sort(array, low, p - 1)
            self.quick_sort(array, p + 1, high)


class QuickSortNoinplace_2(object):
    """
    无 partition 分区函数
    """

    def sort(self, array):
        array = self.quick_sort(array)
        return array

    def quick_sort(self, array):
        if len(array) <= 1:
            return array
        else:
            value = array[-1]
            left, right = [], []
            for i in array[:-1]:
                if i <= value:
                    left.append(i)
                else:
                    right.append(i)
            return self.quick_sort(left) + [value] + self.quick_sort(right)


class QuickSortInplace(object):
    def sort(self, array):
        self.quick_sort(array, 0, len(array) - 1)
        return array

    def patition(self, array, low, high):
        pivot = array[high]
        j = low
        for i in range(low, high):
            if array[i] <= pivot:
                array[i], array[j] = array[j], array[i]
                j += 1
            else:
                continue
        array[high], array[j] = array[j], array[high]
        return j

    def quick_sort(self, array, low, high):
        if low >= high:
            return
        else:
            p = self.patition(array, low, high)
            self.quick_sort(array, low, p - 1)
            self.quick_sort(array, p + 1, high)


class QuickSortInplace_random(object):
    def sort(self, array):
        self.quick_sort(array, 0, len(array) - 1)
        return array

    def patition(self, array, low, high):
        pivot = array[high]
        j = low
        for i in range(low, high):
            if array[i] <= pivot:
                array[i], array[j] = array[j], array[i]
                j += 1
            else:
                continue
        array[high], array[j] = array[j], array[high]
        return j

    def quick_sort(self, array, low, high):
        if low >= high:
            return
        else:
            # random position
            r = np.random.randint(low, high)
            array[r], array[high] = array[high], array[r]

            p = self.patition(array, low, high)
            self.quick_sort(array, low, p - 1)
            self.quick_sort(array, p + 1, high)


def cal_sort(sortfn, arr):
    stime = time.time()
    sorted_arr = sortfn.sort(arr)
    etime = time.time()
    return etime - stime, sorted_arr


def is_sorted(a, b):
    try:
        return (a == b).all()
    except AttributeError:
        return (a == b) is True


def tetSort(n):
    types = ['all one', 'ordered', 're_order', 'random']
    for i in [MergeSort_1, MergeSort_2, QuickSortNoinplace_1, QuickSortNoinplace_2, QuickSortInplace,
              QuickSortInplace_random]:
        # for i in [QuickSortNoinplace_inplace_random]:
        arrs = [np.ones(n), np.arange(n), np.arange(n, 0, -1), np.random.randint(0, n, n)]
        for typ, arr in zip(types, arrs):
            arr_copy = arr.copy()
            sortfn = i()
            time, sorted_arr = cal_sort(sortfn, arr)
            print('{} time {} consumed {}'.format(i.__name__, typ, time))
            truesorted = sorted(arr_copy)
            assert is_sorted(sorted_arr, truesorted)


if __name__ == '__main__':
    arrs = np.array([4, 5, 6, 1, 2, 3, ])
    # ms1 = MergeSort_2()
    # arrs = ms1.sort(arrs)
    arrs = np.array([4, 5, 6, 1, 2, 3, 1])
    # qs1 = QuickSortNoinplace_1()
    # qs1.sort(arrs)
    # print(arrs)
    n = 500
    tetSort(n)
