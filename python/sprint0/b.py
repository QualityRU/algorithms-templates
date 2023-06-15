from typing import List, Tuple

def zipper(n: int, a: List[int], b: List[int]) -> List[int]:
    merged = []
    for i in range(n):
        merged.append(a[i])
        merged.append(b[i])
    return merged

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return n, a, b

n, a, b = read_input()
print(" ".join(map(str, zipper(n, a, b))))
