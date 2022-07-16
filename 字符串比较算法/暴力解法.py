def fun1(s: str, p: str):
    """BF算法，即暴力算法"""
    # caution: 此算法有问题
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


def fun2(s: str, p: str):
    """复制内存了，可以这样吗"""
    p_len = len(p)
    for idx, i in enumerate(s):
        if s[idx: idx + p_len] == p:
            return idx
    return -1


def fun3(s: str, p: str):
    """严格按照n * m 进行判断的思想, 并且不需要将第一个字符串匹配完全"""
    len_p = len(p)
    len_s = len(s)
    if len_p > len_s:
        return -1
    for i in range(0, len_s - len_p + 1):
        for j, k in zip(range(i, len_p + i), range(len_p)):
            if s[j] != p[k]:
                break
            elif k == len_p - 1:
                return j - len_p + 1
    return -1


if __name__ == '__main__':
    s = "hello world"
    # p = 'llo -'
    # p = 'llo '
    # p = 'hel'
    # p = 'lo w'
    # p = 'lo wl'
    p = 'ld'

    ret = fun3(s, p)
    print(ret)
