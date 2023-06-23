# Контест ID: 88464571

from typing import List


def factorize(number: int) -> List[int]:
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors


result = factorize(int(input()))
print(' '.join(map(str, result)))
