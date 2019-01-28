def full_permutation(array, length, depth):
    print_permutation(array, length, depth)


def print_permutation(array, length, depth):
    # print('depth,', depth)
    if depth == 1:
        print(' '.join(map(str, array)))

    for i in range(depth):
        array[i], array[depth - 1] = array[depth - 1], array[i]
        print_permutation(array, length, depth - 1)
        array[depth - 1], array[i] = array[i], array[depth - 1]


array = [1, 2, 3]
full_permutation(array, len(array), len(array))
