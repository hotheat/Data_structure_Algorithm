def bsearch_sqrt(num: int):
    # num 是小数的情况注意
    low, high = 0.0, max(1.0, num)
    value = low
    while len(str(value).split('.')[1]) < 6:
        value = (low + high) / 2
        if pow(value, 2) < num:
            low = value
        elif pow(value, 2) > num:
            high = value
        else:
            return value
    return value


if __name__ == '__main__':
    num = 6
    print(bsearch_sqrt(num))
    num = 0.5
    print(bsearch_sqrt(num))
    num = 4
    print(bsearch_sqrt(num))
