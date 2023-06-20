# Контест ID:


def is_power_of_four(number: int) -> bool:
    if number <= 0:
        return False
    while number % 4 == 0:
        number //= 4
    return number == 1


print(is_power_of_four(int(input())))
