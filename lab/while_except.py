def fun():
    i = 0
    while i < 100:
        i += 1

        try:
            if i == 50:
                raise IndexError
        except IndexError:
            break
    return i


if __name__ == '__main__':
    ret = fun()
    print(ret)
