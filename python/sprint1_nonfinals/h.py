# Контест ID:

from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    max_len = max(len(first_number), len(second_number))
    first_number = first_number.zfill(max_len)
    second_number = second_number.zfill(max_len)

    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        digit_sum = int(first_number[i]) + int(second_number[i]) + carry
        result = str(digit_sum % 2) + result
        carry = digit_sum // 2

    if carry:
        result = '1' + result

    return result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
