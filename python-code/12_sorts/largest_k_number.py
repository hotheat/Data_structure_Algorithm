class Largest_K(object):
    """
    O(n) 时间复杂度内寻找第 k 大数
    """
    def k_largest(self, array, k: int):
        value = self.find_k(array, 0, len(array) - 1, k)
        return value

    def partition(self, array, low, high):
        # 与快排相反，比 pivot 大的放左边，比 pivot 小的放右边
        j = low
        pivot = array[high]
        for i in range(low, high):
            if array[i] > pivot:
                array[i], array[j] = array[j], array[i]
                j += 1
        array[j], array[high] = array[high], array[j]
        return j

    def find_k(self, array, low, high, k):
        p = self.partition(array, low, high)
        if k == p + 1:
            return array[p]
        elif k > p + 1:
            return self.find_k(array, p+1, high, k)
        else:
            return self.find_k(array, low, p-1, k)


if __name__ == '__main__':
    arr = [3, 5, 7, 8, 2, 1, 2]
    k = 2
    lk = Largest_K()
    print(lk.k_largest(arr, k))
