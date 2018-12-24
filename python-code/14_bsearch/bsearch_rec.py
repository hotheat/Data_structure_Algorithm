def bisearch(array, target):
    return bs(array, 0, len(array), target)


def bs(array, low, high, target):
    if low > high:
        return -1
    else:
        mid = low + (high - low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return bs(array, mid + 1, high, target)
        else:
            return bs(array, low, mid - 1, target)


if __name__ == '__main__':
    array = [2, 3, 5, 6, 8]
    target = 4
    print(bisearch(array, target))
    target = 5
    print(bisearch(array, target))
