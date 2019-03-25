def rmatched(regex, main, r_idx, m_idx):
    global is_matched
    if is_matched is True:
        return
    # 正则串和主串都到达末尾，已经匹配上
    if r_idx >= len(regex) and m_idx >= len(main):
        is_matched = True
        return
    # 主串没匹配完，但正则串还有，
    # 或者主串没匹配完，正则串已经没了，说明没有匹配上
    if m_idx >= len(main) and r_idx < len(regex) or \
            (m_idx < len(main) and r_idx >= len(regex)):
        is_matched = False
        return

    if regex[r_idx] == '*':
        # * 匹配任意字符，递归搜索每一种情况
        for i in range(m_idx, len(main)):
            rmatched(regex, main, r_idx + 1, i + 1)

    elif regex[r_idx] == '?':
        rmatched(regex, main, r_idx + 1, m_idx + 1)
        rmatched(regex, main, r_idx + 1, m_idx)

    else:
        if regex[r_idx] == main[m_idx]:
            rmatched(regex, main, r_idx + 1, m_idx + 1)


if __name__ == '__main__':
    regex = 'abc*d?ef'
    main_strs = ['abcbcfsddef', 'abcbcfsddeef', 'abcbcfsddefe']

    for m in main_strs:
        is_matched = False
        rmatched(regex, m, 0, 0)
        print(is_matched)
