# Контест ID: 89021419


def binary_search(arr: list, left: int, right: int, target: int) -> int:
    if left > right:
        return -1

    mid: int = (left + right) // 2
    arr_left: int = arr[left]
    arr_right: int = arr[right]
    arr_mid: int = arr[mid]

    if arr_mid == target:
        return mid

    if arr_left <= arr_mid and arr_left <= target < arr_mid:
        right = mid - 1
    elif arr_left <= arr_mid or arr_mid < target <= arr_right:
        left = mid + 1
    else:
        right = mid - 1

    return binary_search(arr, left, right, target)


def broken_search(nums: list, target: int) -> int:
    left: int = 0
    right: int = len(nums) - 1
    return binary_search(nums, left, right, target)


if __name__ == '__main__':

    def test():
        arr: list = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr, 5) == 6
