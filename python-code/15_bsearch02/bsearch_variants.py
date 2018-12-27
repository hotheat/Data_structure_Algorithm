def bsearch_first_equal(array, target):
    """
    在从小到大排列的数组中，查找第一个值等于给定值的元素索引
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        elif mid == 0 or (array[mid - 1] != target):
            return mid
        else:
            high = mid - 1
    return -1


def bsearch_last_equal(array, target):
    """
    在从小到大排列的数组中，查找最后一个值等于给定值的元素索引
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        elif mid == len(array) - 1 or (array[mid + 1] != target):
            return mid
        else:
            low = mid + 1
    return -1


def bsearch_first_egreater(array, target):
    """
    查找第一个大于等于给定值的元素索引
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] >= target:
            if mid == 0 or array[mid - 1] < target:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


def bsearch_last_eless(array, target):
    """
    查找第一个大于等于给定值的元素索引
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] <= target:
            if mid == len(array) - 1 or array[mid + 1] > target:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    array = [1, 3, 4, 5, 5, 5, 6, 6, 8, 9]
    target = 6
    assert bsearch_first_equal(array, target) == 6
    assert bsearch_last_equal(array, target) == 7
    target = 2
    assert bsearch_first_egreater(array, target) == 1
    target = 7
    assert bsearch_last_eless(array, target) == 7
    target = 5
    assert bsearch_first_equal(array, target) == 3
    assert bsearch_last_equal(array, target) == 5
    assert bsearch_first_egreater(array, target) == 3
    assert bsearch_last_eless(array, target) == 5
    array = [5] * 10
    target = 5
    assert bsearch_first_equal(array, target) == 0
    assert bsearch_last_equal(array, target) == len(array) - 1
