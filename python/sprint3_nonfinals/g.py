# 88953278


def sort_numbers(numbers):
    less = []
    equal = []
    greater = []
    for x in numbers:
        if x == '0':
            less.append(x)
        elif x == '1':
            equal.append(x)
        else:
            greater.append(x)
    return less + equal + greater


if __name__ == '__main__':
    n = int(input())
    numbers = input().split()
    sorted_numbers = sort_numbers(numbers)
    print(*sorted_numbers)
