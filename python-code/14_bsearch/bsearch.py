def bisearch(array, target):
    """
    没有重复元素的，已排序的数组，如果数据存在，则返回索引，如果不存在，则返回 -1
    注意，循环终止条件，mid 的计算以及 mid 的取值
    """
    low, high = 0, len(array)
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    array = [2, 3, 5, 6, 8]
    target = 4
    print(bisearch(array, target))
    target = 5
    print(bisearch(array, target))
