# Контест ID:

from typing import Tuple


def get_sum(first_number: str, second_number: str) -> str:
    max_len = max(len(first_number), len(second_number))
    result = ''
    carry = 0
    bit_mask = 1
    while bit_mask <= max_len:
        bit1 = int(first_number[-bit_mask]) if bit_mask <= len(first_number) else 0
        bit2 = int(second_number[-bit_mask]) if bit_mask <= len(second_number) else 0
        current_sum = bit1 + bit2 + carry
        carry = 1 if current_sum > 1 else 0
        result = str(current_sum % 2) + result
        carry <<= 1
        result <<= 1
        bit_mask <<= 1
    if carry:
        result = '1' + result
    return result


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
