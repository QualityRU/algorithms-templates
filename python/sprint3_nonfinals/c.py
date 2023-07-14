# 88951073


def subsequence(substring, whole_line):
    sub_len = len(substring)
    line_len = len(whole_line)
    i = 0
    j = 0

    while i < sub_len and j < line_len:
        if substring[i] == whole_line[j]:
            i += 1
        j += 1

    return i == sub_len


if __name__ == '__main__':
    substring = input()
    whole_line = input()
    print(subsequence(substring, whole_line))
