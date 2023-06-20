# Контест ID:

from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    result = 0

    if len(temperatures) == 1:
        result += 1
    else:
        for i in range(1, len(temperatures) - 1):
            if (
                temperatures[i] > temperatures[i - 1]
                and temperatures[i] > temperatures[i + 1]
            ):
                result += 1
    return result


def read_input() -> List[int]:
    _ = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
