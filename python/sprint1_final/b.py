# Контест ID: 88296731


def sleight_of_hand(k: int, matrix: str) -> int:
    numbers = [matrix.count(str(i)) for i in range(1, 10)]
    result = sum(1 for n in numbers if n != 0 and n <= k)
    return result


if __name__ == '__main__':
    k = int(input()) * 2
    matrix = ''
    matrix = ''.join([matrix + input() for _ in range(4)])
    print(sleight_of_hand(k, matrix))
