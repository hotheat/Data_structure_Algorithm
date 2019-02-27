"""
对主串的 ml-pl+1 个子串求哈希值，判断模式串哈希值是否与子串相同。
整个算法时间复杂度包括求所有子串哈希值及子串与模式串哈希值的比较
1. 利用上一个已经计算好的子串哈希值求下一个子串哈希值
2. 子串哈希值存放在数组中，直接读取即可
3. 存在哈希冲突时，再判断两个子串是否相等
"""


def simple_hash(s, start, end):
    assert start < end
    res = 0
    for i in range(start, end):
        res += ord(s[i])

    return res


def rabin_karp(main, pattern):
    ml = len(main)
    pl = len(pattern)

    if ml <= pl:
        return False if ml < pl else True

    hash_res = [None] * (ml - pl + 1)
    hash_res[0] = simple_hash(main, 0, pl)
    for i in range(1, ml - pl + 1):
        hash_res[i] = hash_res[i - 1] - ord(main[i - 1]) + ord(main[i + pl - 1])

    hashp = simple_hash(pattern, 0, pl)
    
    for i, v in enumerate(hash_res):
        if v == hashp and pattern == main[i:i + pl]:
            return True
        else:
            continue

    return False


if __name__ == '__main__':
    main = 'abbcdd'
    p1 = 'bbc'
    p2 = 'bcc'
    print(rabin_karp(main, p1))
    print(rabin_karp(main, p2))
