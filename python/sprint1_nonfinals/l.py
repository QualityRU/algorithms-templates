# Контест ID: 88464873

from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    return chr(sum(map(ord, longer)) - sum(map(ord, shorter)))


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
