# Контест ID: 88376334


def is_palindrome(line: str) -> bool:
    line = [w for w in line.lower() if w.isalnum()]
    return line == line[::-1]


print(is_palindrome(input().strip()))
