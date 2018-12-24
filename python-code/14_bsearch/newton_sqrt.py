def newton_sqrt(num):
    value = num / 2
    while abs(value ** 2 - num) >= 1e-5:
        value = value - (value ** 2 - num) / (2 * value)
    return value


if __name__ == '__main__':
    num = 6
    print(newton_sqrt(num))
    num = 0.5
    print(newton_sqrt(num))
    num = 4
    print(newton_sqrt(num))
