def hash_func(string):
    """
    caution: 14个z就会超出 long 所能存储的最大值
    """
    key_map = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25
    }
    len_s = len(string)
    h = 0
    for idx, i in enumerate(string):
        pivot = len_s - idx - 1
        print(pivot)
        h += key_map[i] * (26 ** pivot)
    return h


def fun(s, p):
    pass


if __name__ == '__main__':
    print(hash_func('cba'))
