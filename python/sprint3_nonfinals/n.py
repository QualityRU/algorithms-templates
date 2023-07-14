# 88950846


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merged = []
    current_interval = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= current_interval[1]:
            current_interval = (
                current_interval[0],
                max(interval[1], current_interval[1]),
            )
        else:
            merged.append(current_interval)
            current_interval = interval

    merged.append(current_interval)

    return merged


def find_flowerbeds(n, intervals):
    if n == 0:
        return []

    merged_intervals = merge_intervals(intervals)

    flowerbeds = []

    for interval in merged_intervals:
        if interval[0] != interval[1]:
            flowerbeds.append(interval)

    return flowerbeds


if __name__ == '__main__':
    n = int(input())
    intervals = []
    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append((start, end))

    result = find_flowerbeds(n, intervals)

    for flowerbed in result:
        print(flowerbed[0], flowerbed[1])
