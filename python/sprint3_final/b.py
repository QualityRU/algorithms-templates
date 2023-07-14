# Контест ID: 89021830


def partition(players: list, left: int, right: int) -> list:
    NAME: int = 0
    SOLVED: int = 1
    PENALTY: int = 2

    pivot: list = players[left]
    i_left: int = left + 1
    i_right: int = right

    while i_left <= i_right:
        while i_left <= i_right and (
            players[i_left][SOLVED] > pivot[SOLVED]
            or (
                players[i_left][SOLVED] == pivot[SOLVED]
                and players[i_left][PENALTY] < pivot[PENALTY]
            )
            or (
                players[i_left][SOLVED] == pivot[SOLVED]
                and players[i_left][PENALTY] == pivot[PENALTY]
                and players[i_left][NAME] < pivot[NAME]
            )
        ):
            i_left += 1

        while i_left <= i_right and (
            players[i_right][SOLVED] < pivot[SOLVED]
            or (
                players[i_right][SOLVED] == pivot[SOLVED]
                and players[i_right][PENALTY] > pivot[PENALTY]
            )
            or (
                players[i_right][SOLVED] == pivot[SOLVED]
                and players[i_right][PENALTY] == pivot[PENALTY]
                and players[i_right][NAME] > pivot[NAME]
            )
        ):
            i_right -= 1

        if i_left <= i_right:
            players[i_left], players[i_right] = (
                players[i_right],
                players[i_left],
            )

            i_left += 1
            i_right -= 1

    players[left], players[i_right] = players[i_right], players[left]
    return i_right


def quick_sort(players: list, left: int, right: int) -> None:
    if left < right:
        p = partition(players, left, right)
        quick_sort(players, left=left, right=p - 1)
        quick_sort(players, left=p + 1, right=right)


if __name__ == '__main__':
    n: int = int(input())
    players: list = list()

    for _ in range(n):
        name, solved, penalty = input().split()
        players.append((name, int(solved), int(penalty)))

    quick_sort(players, left=0, right=n - 1)

    for name, _, _ in players:
        print(name)
