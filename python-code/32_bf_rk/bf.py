def brute_froce(main, pattern):
    ml = len(main)
    pl = len(pattern)
    if ml <= pl:
        return False if ml < pl else True

    for i in range(0, ml - pl + 1):
        for j in range(0, pl):
            print(main[i+j], pattern[j], i, j)
            if main[i + j] == pattern[j]:
                # 找到完全匹配的子串
                if j == pl - 1:
                    return True
                else:
                    continue
            # 发现不匹配的字符，寻找下一个子串
            else:
                break
    return False


if __name__ == '__main__':
    main = 'abbcdd'
    p1 = 'bbc'
    p2 = 'bcc'
    print(brute_froce(main, p1))
    print(brute_froce(main, p2))
