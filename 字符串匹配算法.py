def fun1(s: str, p: str):
    """BF算法，即暴力算法"""
    if not p:
        return -1

    i = j = 0

    start = None
    start_flag = False

    length_p = len(p)
    # caution: while True, 通过index_error跳出循环更好
    while i < length_p and j < len(s) - length_p:
        if p[i] != s[j]:
            j += 1
            i = 0
            start = None
        else:
            if not start_flag:
                start = j
                start_flag = True
            i += 1
            j += 1
    if i == length_p:
        return start
    return -1


if __name__ == '__main__':
    s = "hello world"
    # p = 'llo -'
    # p = 'llo '
    p = 'hel'

    ret = fun1(s, p)
    print(ret)
