# Контест ID: 88254166

L = 10**9


def check_parity(a: int, b: int, c: int) -> bool:
    if a > L or b > L or c > L:
        raise 'Числа не должны превосходят 10^9 по модулю.'
    if a % 2 == b % 2 == c % 2:
        result = True
    else:
        result = False
    return result


def print_result(result: bool) -> None:
    if result:
        print('WIN')
    else:
        print('FAIL')


a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
