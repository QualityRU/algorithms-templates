# Контест ID: 88218095

from typing import List, Optional, Tuple


def two_sum2(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    previous = set()

    for A in arr:
        Y = target_sum - A
        if Y in previous:
            return A, Y
        else:
            previous.add(A)

    return None


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    arr.sort()

    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return arr[left], arr[right]
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(' '.join(map(str, result)))


arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
