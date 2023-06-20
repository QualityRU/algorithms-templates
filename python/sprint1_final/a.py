# Контест ID: 88296532

from typing import List, Tuple


def nearest_zero(streets: List[int]) -> Tuple[List[int], int]:
    n = len(streets)
    result = [0] * n
    zero_list = [i for i in range(n) if streets[i] == '0']

    for house in range(0, zero_list[0] + 1):
        result[house] = zero_list[0] - house

    for pos in range(len(zero_list) - 1):
        zero_1, zero_2 = zero_list[pos], zero_list[pos + 1]
        for house in range(zero_1, zero_2):
            result[house] = min(house - zero_1, zero_2 - house)

    for house in range(zero_list[-1], n):
        result[house] = house - zero_list[-1]

    return result


if __name__ == '__main__':
    _ = input()
    streets = list(input().strip().split())
    print(' '.join(map(str, nearest_zero(streets))))
