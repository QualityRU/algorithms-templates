# Контест ID: 88254201

from typing import List, Tuple

L = 1000


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    result = []
    if row > 0:
        result.append(matrix[row - 1][col])
    if row < len(matrix) - 1:
        result.append(matrix[row + 1][col])
    if col > 0:
        result.append(matrix[row][col - 1])
    if col < len(matrix[0]) - 1:
        result.append(matrix[row][col + 1])
    return sorted(result)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    if n > L or m > L:
        raise 'Числа m и n не должны превосходить 1000 по модулю.'
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(' '.join(map(str, get_neighbours(matrix, row, col))))
