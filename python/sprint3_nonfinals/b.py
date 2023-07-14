# 88927272


def combinations(input_string):
    d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    if len(input_string) == 0:
        return ['']

    data = []
    first_digit = input_string[0]
    remaining_digits = input_string[1:]

    for letter in d[first_digit]:
        for combination in combinations(remaining_digits):
            data.append(letter + combination)

    return data


if __name__ == '__main__':
    input_string = input()
    print(' '.join(combinations(input_string)))
