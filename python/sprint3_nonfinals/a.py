# 88914523


def gen(n, opens, result):
    if n == opens == 0:
        print(result)

    if n == 0:
        return

    gen(n - 1, opens + 1, result + '(')

    if opens > 0:
        gen(n - 1, opens - 1, result + ')')


if __name__ == '__main__':
    n = int(input())
    gen(2 * n, 0, '')
